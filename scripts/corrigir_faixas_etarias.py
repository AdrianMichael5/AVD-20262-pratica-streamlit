# [IA] Codex (OpenAI) - correção reproduzível dos rótulos etários na EDA e no CSV.
"""Migração idempotente dos rótulos, preservando os grupos e valores originais.

Executar na raiz: python scripts/corrigir_faixas_etarias.py
Saídas do notebook a partir da alteração são limpas, pois exigem reexecução.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROTULOS = {"<45": "Até 45", "45-54": "46–55", "55-64": "56–65", "65+": "Acima de 65"}

csv_path = ROOT / "data/clean/dataset.csv"
original = csv_path.read_bytes().decode("utf-8")
if "faixa_etaria" not in original.splitlines()[0]:
    raise SystemExit("Script histórico de Heart Disease: não altera o CSV College atual.")
linhas = original.splitlines(keepends=True)
for i, linha in enumerate(linhas[1:], start=1):
    corpo = linha.rstrip("\r\n")
    prefixo, faixa = corpo.rsplit(",", 1)
    linhas[i] = prefixo + "," + ROTULOS.get(faixa, faixa) + linha[len(corpo):]
csv_path.write_bytes("".join(linhas).encode("utf-8"))

nb_path = ROOT / "notebooks/eda.ipynb"
notebook = json.loads(nb_path.read_text(encoding="utf-8"))
alterado = False
for cell in notebook["cells"]:
    source = "".join(cell["source"])
    if 'df["faixa_etaria"] = pd.cut' in source and 'labels=["<45"' in source:
        for anterior, novo in ROTULOS.items():
            source = source.replace(f'"{anterior}"', f'"{novo}"')
        source = source.replace('bins=[0, 45, 55, 65, 100],', 'bins=[0, 45, 55, 65, 100], right=True,')
        source = '# Limites preservados: (0,45], (45,55], (55,65], (65,100].\n' + source
        cell["source"] = source.splitlines(keepends=True)
        alterado = True
    if alterado and cell["cell_type"] == "code":
        cell["outputs"] = []
        cell["execution_count"] = None
if alterado:
    nb_path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("Rótulos corrigidos; CSV preservado nas demais colunas. Notebook exige reexecução após a célula alterada.")
