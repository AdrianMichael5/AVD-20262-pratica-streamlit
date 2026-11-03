# [IA] Codex (OpenAI) - adaptação técnica do notebook College fornecido pelo autor.
"""Preserva o original; produz notebooks/eda.ipynb sem os trechos médicos residuais."""
import json
from pathlib import Path
import re

import nbformat

ROOT = Path(__file__).resolve().parents[1]
original = ROOT / "Cópia_de_Aula_11_Prática_EDA.ipynb"
nb = nbformat.read(original, as_version=4)
cells = []
for i, cell in enumerate(nb.cells):
    source = cell.source
    if i == 0:
        cell.source = """# EDA — College.csv

**Autor responsável:** Adrian Michael. **Origem:** notebook individual fornecido pelo autor, adaptado do material da disciplina Análise e Visualização de Dados (Cesar School, 2026.2).

O arquivo original declara assistência de Colab AI/Gemini em código, textos e conclusões. Esses relatos não foram apagados nem convertidos em autoria exclusiva do aluno. Os ajustes técnicos do Codex estão marcados com `[IA]`.

**Tema confirmado pelo autor:** College.csv (pedido: “use college.csv”). A fonte usada é a mesma Kaggle do notebook original; o [manual ISLR](https://cran.r-project.org/web/packages/ISLR/ISLR.pdf) documenta as variáveis. São dados históricos de instituições de ensino dos EUA, não custos ou indicadores atuais.

**Reprodução:** instalar `requirements-dev.txt` e executar do início ao fim. O carregamento utiliza `data/raw/College.csv`; se ausente, o script de importação obtém a fonte pública. A exportação final gera o CSV que o app usa localmente, sem login no Kaggle durante sua execução.

**Limites de autoria:** as conclusões preexistentes assistidas por Gemini precisam de validação/revisão pessoal. O Codex não redigiu novas conclusões ou justificativas em nome do autor. Veja [declaração de IA](../prompts/declaracao-uso-ia.md).
"""
    elif i == 4:
        cell.source = """# [IA] Codex (OpenAI) - carregamento reproduzível da mesma base pública do notebook original.
from pathlib import Path
import sys

RAIZ = Path.cwd() if (Path.cwd() / "app.py").exists() else Path.cwd().parent
sys.path.insert(0, str(RAIZ / "scripts"))
from importar_college import COLS, main as importar_college

ARQUIVO_RAW = RAIZ / "data/raw/College.csv"
if not ARQUIVO_RAW.exists():
    importar_college()
df = pd.read_csv(ARQUIVO_RAW)[COLS].copy()
df.head()
"""
    elif i < 121 and cell.cell_type == "markdown" and re.search(r"Heart Disease|doenca_cardiaca|\bchol\b|\bthalach\b|\bca\b|\bthal\b|paciente|cardíac|clinicamente|fisiolog|sexo e faixa", source, re.I):
        # Material da demonstração médica permanece no arquivo original, sem contaminar College.
        continue
    elif cell.cell_type == "markdown" and "data:image" in source:
        # Screenshot de referência sem vínculo com execução atual; original preservado.
        continue
    if cell.cell_type == "markdown":
        if source.startswith("## Principais Conclusões"):
            cell.source = "> **Texto preexistente com assistência de Gemini, conforme declaração do original. Validação e revisão individual pendentes; esta execução não certifica as interpretações.**\n\n" + source
        elif source.startswith("## Declaração de Uso"):
            cell.source = "> **Relato de IA preservado do arquivo fornecido. Complementado pela declaração atual em prompts/.**\n\n" + source
        elif source.startswith("## Justificativa das Decisões"):
            cell.source = "> **Justificativa preexistente assistida por Gemini; conferir pessoalmente. Não substitui justificativa das métricas do Dashboard 2.**\n\n" + source
        elif source.startswith("## Hands-on!"):
            cell.source = "## Revisão individual\n\nAs perguntas didáticas são um roteiro. Revisar as respostas e as conclusões preexistentes com suas próprias palavras. A justificativa das métricas está em [entregas/justificativa-metricas.md](../entregas/justificativa-metricas.md)."
        elif source.strip() == "*Resposta*:":
            cell.source = "**Resposta individual:** pendente de revisão/preenchimento do autor."
        elif "Pearson" in source and "exige normalidade" in source:
            cell.source = """### Correlação — nota técnica [IA] Codex (OpenAI)

Pearson é um resumo descritivo de associação linear; Spearman e Kendall usam postos. O cálculo descritivo de Pearson não exige normalidade; premissas adicionais entram na inferência. A célula seguinte mantém a comparação dos três métodos do notebook original.

[Documentação SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html).
"""
        elif "nenhuma" in source and "Shapiro" in source and "tecnicamente" in source:
            cell.source = "**Nota técnica [IA] Codex (OpenAI):** um teste de normalidade da amostra completa não testa normalidade por grupo. A célula mantém Welch e Mann-Whitney como comparação metodológica; a interpretação cabe ao autor. [SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html)."
    source = cell.source
    source = source.replace("Aplicativos", "Candidaturas").replace("aplicativos", "candidaturas")
    if cell.cell_type == "code":
        if "# [IA]" not in source:
            source = "# [IA] Codex (OpenAI) - integração técnica do código fornecido; apoio Gemini prévio conforme declaração.\n" + source
        if "g = sns.PairGrid(df[VARS_QUANT]" in source:
            source = "# [IA] Codex (OpenAI) - correlograma legível com as cinco variáveis já comparadas na EDA.\n" + source.replace("sns.PairGrid(df[VARS_QUANT]", "sns.PairGrid(df[variables_to_compare]")
        if 'figsize=(7, 6)' in source and 'df[VARS_QUANT].corr' in source:
            source = source.replace('figsize=(7, 6)', 'figsize=(14, 12)')
        # Elimina metadados/saídas de execuções antigas; serão geradas novamente.
        cell.outputs = []
        cell.execution_count = None
        cell.metadata = {}
    cell.source = source
    cells.append(cell)

cells.append(nbformat.v4.new_markdown_cell("""## Exportação para o Streamlit

**[IA] Codex (OpenAI) — integração técnica com o app.** Mantidas as 18 variáveis da base, mais `Expend_log` e os tercis `Apps_binned` já calculados nesta EDA. Nenhuma linha é excluída e `Grad.Rate` não é truncada; eventuais valores acima de 100 permanecem para revisão do autor.
"""))
cells.append(nbformat.v4.new_code_cell("""# [IA] Codex (OpenAI) - exportação e verificações técnicas, sem interpretação individual.
PASTA_CLEAN = RAIZ / "data/clean"
PASTA_CLEAN.mkdir(parents=True, exist_ok=True)
colunas_exportadas = COLS + ["Expend_log", "Apps_binned"]
assert len(df) == 777
assert not df[colunas_exportadas].isna().any().any()
df[colunas_exportadas].to_csv(PASTA_CLEAN / "dataset.csv", index=False, lineterminator="\\n")
print(f"College exportado: {len(df)} instituições, {len(colunas_exportadas)} colunas.")
"""))
nb.cells = cells
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}
(ROOT / "notebooks/eda.ipynb").write_bytes(nbformat.writes(nb).replace("\r\n", "\n").encode("utf-8"))
print(f"Notebook College preparado: {len(cells)} células; original preservado.")
