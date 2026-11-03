# [IA] Codex (OpenAI) - leitura estrutural da assinatura e apuração de resultados da EDA.
"""Não altera o PDF nem substitui validação criptográfica pelo ITI."""
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from pypdf import PdfReader
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
VARS = ["Apps", "Accept", "Enroll", "Top10perc", "Top25perc", "F.Undergrad", "P.Undergrad", "Outstate", "Room.Board", "Books", "Personal", "PhD", "Terminal", "S.F.Ratio", "perc.alumni", "Expend", "Grad.Rate"]


def ajustar_holm(pvalues):
    values = np.asarray(pvalues, dtype=float)
    if not len(values):
        return values.copy()
    order = np.argsort(values)
    adjusted = np.minimum(1, np.maximum.accumulate(values[order] * np.arange(len(values), 0, -1)))
    output = np.empty_like(values)
    output[order] = adjusted
    return output


def resultados(df):
    raw = df[["Private", *VARS]]
    testes = []
    for var in VARS:
        a, b = df.loc[df.Private.eq("No"), var], df.loc[df.Private.eq("Yes"), var]
        testes.append({"variavel": var, "p_mannwhitney": float(stats.mannwhitneyu(a, b).pvalue), "p_welch": float(stats.ttest_ind(a, b, equal_var=False).pvalue)})
    table = pd.DataFrame(testes)
    # Holm: ordem crescente, multiplicação por m-i, máximo acumulado e limite 1.
    table["p_holm"] = ajustar_holm(table.p_mannwhitney)
    contingency = pd.crosstab(df.Private, df.Apps_binned).reindex(index=["No", "Yes"], columns=["Baixo", "Médio", "Alto"])
    chi = stats.chi2_contingency(contingency)
    pearson, spearman = df[VARS].corr(), df[VARS].corr(method="spearman")
    delta = (pearson - spearman).abs()
    np.fill_diagonal(delta.values, 0)
    pair = delta.stack().idxmax()
    return {
        "n": len(df), "ausentes": int(raw.isna().sum().sum()), "duplicadas": int(raw.duplicated().sum()),
        "tipos": df.Private.value_counts().to_dict(),
        "skewness_expend": [float(df.Expend.skew()), float(df.Expend_log.skew())],
        "shapiro_expend": float(stats.shapiro(df.Expend).pvalue),
        "shapiro_rejeitados": sum(stats.shapiro(df[v]).pvalue < .05 for v in VARS),
        "shapiro_nao_rejeitados": [v for v in VARS if stats.shapiro(df[v]).pvalue >= .05],
        "spearman_apps": spearman.loc["Apps", ["Accept", "Enroll", "Expend"]].to_dict(),
        "maior_divergencia_correlacao": {"par": list(pair), "pearson": float(pearson.loc[pair]), "spearman": float(spearman.loc[pair])},
        "medias_por_tipo": df.groupby("Private")[["Apps", "Accept", "Enroll", "Expend", "Grad.Rate"]].mean().round(3).to_dict(orient="index"),
        "testes": table.to_dict(orient="records"),
        "chi2": float(chi.statistic), "p_chi2": float(chi.pvalue), "esperado_minimo": float(chi.expected_freq.min()),
        "cramer_v": float(stats.contingency.association(contingency.to_numpy(), method="cramer")),
        "proporcoes_tercis": contingency.div(contingency.sum(axis=1), axis=0).round(4).to_dict(orient="index"),
        "graduacao_acima_100": int(df["Grad.Rate"].gt(100).sum()), "graduacao_maxima": int(df["Grad.Rate"].max()),
    }


def main():
    pdf = ROOT / "prompts/DECLARACAO_IA_assinado.pdf"
    reader = PdfReader(pdf)
    signatures = []
    for name, field in (reader.get_fields() or {}).items():
        if field.get("/FT") == "/Sig" and field.get("/V"):
            value = field["/V"].get_object()
            signatures.append({"campo": name, "byte_range": list(value.get("/ByteRange", [])), "conteudo_presente": bool(value.get("/Contents"))})
    print(json.dumps({"pdf_paginas": len(reader.pages), "assinaturas_estruturais": signatures,
                      "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest()}, ensure_ascii=False, indent=2))
    if "--somente-assinatura" in sys.argv:
        import pymupdf
        folder = ROOT / "tmp/pdfs"
        folder.mkdir(parents=True, exist_ok=True)
        with pymupdf.open(pdf) as document:
            document[4].get_pixmap(matrix=pymupdf.Matrix(1.1, 1.1)).save(folder / "assinada-pagina5.png")
        return
    print(json.dumps(resultados(pd.read_csv(ROOT / "data/clean/dataset.csv")), ensure_ascii=False, indent=2, default=int))


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    main()
