# [IA] Codex (OpenAI) - obtenção e preparação reprodutível de College.csv.
"""Baixa a fonte pública do notebook e exporta as transformações existentes."""
from datetime import datetime
import hashlib
import io
import json
from pathlib import Path
import zipfile

import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
KAGGLE = "https://www.kaggle.com/api/v1/datasets/download/nitishsubandh/dataset/College.csv"
OFFICIAL = "https://www.statlearning.com/s/College.csv"
COLS = ["Private", "Apps", "Accept", "Enroll", "Top10perc", "Top25perc", "F.Undergrad", "P.Undergrad", "Outstate", "Room.Board", "Books", "Personal", "PhD", "Terminal", "S.F.Ratio", "perc.alumni", "Expend", "Grad.Rate"]


def main():
    raw_path = ROOT / "data/raw/College.csv"
    if raw_path.exists():
        payload = raw_path.read_bytes()
        anterior = ROOT / "data/clean/college-manifesto.json"
        source = json.loads(anterior.read_text(encoding="utf-8")).get("fonte_obtida", "cache local") if anterior.exists() else "cache local data/raw/College.csv"
    else:
        for url in [KAGGLE, OFFICIAL]:
            try:
                response = requests.get(url, timeout=60)
                response.raise_for_status()
                payload = response.content
                if zipfile.is_zipfile(io.BytesIO(payload)):
                    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                        name = next(n for n in archive.namelist() if Path(n).name == "College.csv")
                        payload = archive.read(name)
                candidate = pd.read_csv(io.BytesIO(payload))
                if not set(COLS).issubset(candidate.columns) or len(candidate) != 777:
                    raise ValueError("A resposta não contém o College esperado")
                source = url
                raw_path.write_bytes(payload)
                break
            except (requests.RequestException, ValueError, StopIteration, pd.errors.ParserError) as exc:
                print(f"Fonte indisponível: {url} ({type(exc).__name__}); tentando fonte alternativa.")
        else:
            raise RuntimeError("Não foi possível obter College.csv das fontes públicas.")
    raw = pd.read_csv(io.BytesIO(payload))
    # O notebook de referência usa 18 variáveis, sem nome/index institucional.
    df = raw[COLS].copy()
    assert len(df) == 777 and not df.isna().any().any()
    assert df.Private.isin(["No", "Yes"]).all()
    assert df.Apps.sum() == 2332273  # Conferência adicional da versão ISLR.
    df["Expend_log"] = np.log1p(df["Expend"])
    df["Apps_binned"] = pd.qcut(df["Apps"], q=3, labels=["Baixo", "Médio", "Alto"])
    target = ROOT / "data/clean/dataset.csv"
    target.write_bytes(df.to_csv(index=False, lineterminator="\n").encode("utf-8"))
    manifest = {
        "data": datetime.now().astimezone().isoformat(timespec="seconds"),
        "dataset": "College.csv", "fonte_obtida": source,
        "fonte_notebook_original": "https://www.kaggle.com/datasets/nitishsubandh/dataset",
        "fonte_oficial_alternativa": OFFICIAL,
        "raw_sha256": hashlib.sha256(payload).hexdigest(),
        "clean_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "linhas": len(df), "colunas": list(df.columns),
        "contagens_Private": df.Private.value_counts().to_dict(),
        "transformacoes": ["seleção das mesmas 18 variáveis da EDA original", "Expend_log = log1p(Expend)", "Apps_binned = tercis de Apps da base completa; não recalculados por filtro", "sem exclusão de linhas, sem truncar Grad.Rate"],
    }
    (ROOT / "data/clean/college-manifesto.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    main()
