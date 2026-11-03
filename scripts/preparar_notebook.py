# [IA] Codex (OpenAI) - revisão técnica e identificação da origem didática da EDA.
"""Ajustes reproduzíveis; não preenche análises individuais do aluno."""
import json
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "notebooks/eda.ipynb"
nb = json.loads(path.read_text(encoding="utf-8"))
if not any("fetch_ucirepo" in "".join(c["source"]) for c in nb["cells"]):
    raise SystemExit("Script histórico de Heart Disease: não se aplica ao notebook College atual.")

def texto(cell, value):
    cell["source"] = value.splitlines(keepends=True)

for cell in nb["cells"]:
    source = "".join(cell["source"])
    if source.startswith("# EDA na Prática"):
        texto(cell, """# EDA — Heart Disease e dados para os dashboards

**Responsável:** Adrian Michael. **Disciplina:** Análise e Visualização de Dados, Cesar School, 2026.2.

**Origem:** notebook didático da disciplina, adaptado para o app deste repositório. A base e grande parte do texto/código vieram do material de aula; não são apresentados como criação integral do aluno. Os ajustes técnicos com IA estão identificados por `[IA]`.

**Escopo técnico:** obter os dados UCI, executar a análise existente e exportar o dado tratado usado pelo app. As perguntas didáticas permanecem como roteiro; as respostas, a síntese em 3–5 pontos e a justificativa das métricas devem ser redigidas individualmente pelo autor.

**Fonte:** [Heart Disease — UCI, DOI 10.24432/C52P4X](https://archive.ics.uci.edu/dataset/45/heart+disease), licença CC BY 4.0. A menção do catálogo a quatro bases não significa que este recorte as concatene.

**Execução:** instalar `requirements-dev.txt` e executar da primeira à última célula. Da raiz também é possível usar `python scripts/validar_entrega.py notebook`. O app lê apenas `data/clean/dataset.csv`.

**Assistência:** [registro e pendências da declaração](../prompts/declaracao-uso-ia.md). Cabeçalho e correções técnicas de novembro preparados com Codex (OpenAI).
""")
    elif "!pip install ucimlrepo --quiet" in source:
        texto(cell, source.replace("!pip install ucimlrepo --quiet\n", "# [IA] Codex (OpenAI) - dependências instaladas via requirements-dev.txt, fora do kernel.\n"))
    elif source == "*Resposta*:":
        texto(cell, "**Resposta individual pendente:** escrever com suas palavras a partir da saída acima. Não preenchida pela IA.")
    elif source.startswith("**Conhecimento de Domínio**"):
        texto(cell, """**Dicionário e proveniência — revisão técnica [IA] Codex (OpenAI)**

Consultar o [dicionário oficial da UCI](https://archive.ics.uci.edu/dataset/45/heart+disease): `ca` registra o número de vasos principais visualizados por fluoroscopia; `thal` usa códigos 3 (normal), 6 (defeito fixo) e 7 (defeito reversível). Não confundir `thal` com diagnóstico de talassemia.

As saídas seguintes mostram os ausentes encontrados. Os dados não documentam a causa de cada ausência; custo, protocolo ou condição clínica são hipóteses, não conclusões desta EDA.
""")
    elif source.startswith("### Decidindo o Tratamento dos Dados Ausentes"):
        texto(cell, """### Tratamento dos dados ausentes

**Nota metodológica [IA] Codex (OpenAI):** o código original remove registros com ausência em `ca` ou `thal`, sem imputação. A contagem removida está na saída seguinte. A execução preserva essa escolha; não demonstra que as ausências sejam MCAR/MAR nem que a exclusão seja isenta de viés. A justificativa e a discussão das limitações cabem ao autor.
""")
    elif source.startswith("#### Quantitativa x Quantitativa - Correlação"):
        texto(cell, """#### Quantitativa x quantitativa — correlação

**Revisão conceitual [IA] Codex (OpenAI):** Pearson resume associação linear; Spearman e Kendall resumem associação de postos. A normalidade não é requisito para calcular o coeficiente descritivo de Pearson; hipóteses adicionais entram na inferência e no teste paramétrico associado. Shapiro-Wilk sozinho não escolhe o método de correlação.

A célula compara os três coeficientes. O app usa Pearson explicitamente para exploração descritiva. [Referência: SciPy — pearsonr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html).
""")
    elif source.startswith("#### Quantitativa x Qualitativa: Comparando Grupos"):
        texto(cell, """#### Quantitativa x qualitativa: comparando grupos

**Nota metodológica [IA] Codex (OpenAI):** a célula compara Welch e Mann-Whitney entre classes. Um teste de normalidade da amostra inteira não testa normalidade dentro de cada classe. Mann-Whitney testa igualdade de distribuições e não automaticamente diferença de médias/medianas. A escolha e a interpretação devem considerar a pergunta, os grupos e as premissas.

[Referência: SciPy — mannwhitneyu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html).
""")
    elif source.startswith("**Pra discutir:** os dois testes concordam"):
        texto(cell, """**Discussão individual:** compare Welch e Mann-Whitney sem tomar a normalidade da amostra total como teste das classes. Explique qual hipótese responde à sua pergunta.

**Três ou mais grupos:** a próxima célula compara ANOVA e Kruskal-Wallis para `thalach` entre categorias de `cp`. Os testes têm hipóteses diferentes; as conclusões devem ser discutidas pelo autor.
""")
    elif source.startswith("**Pra discutir:** o Kruskal-Wallis concorda"):
        texto(cell, "**Discussão individual:** compare ANOVA e Kruskal-Wallis, explicite suas hipóteses e evite escolher o teste apenas pela normalidade da amostra completa.")
    elif source.startswith("## Hands-on!"):
        texto(cell, """## Síntese individual — pendente de preenchimento pelo autor

As saídas acima não substituem as respostas pessoais às perguntas didáticas.

- Redigir de 3 a 5 conclusões, indicando resultados e limites.
- Explicar as decisões de tratamento dos ausentes e dos valores extremos.
- Justificar pessoalmente as métricas em [entregas/justificativa-metricas.md](../entregas/justificativa-metricas.md).
- Revisar a [declaração de uso de IA](../prompts/declaracao-uso-ia.md), preencher a reflexão e assinar o PDF exigido.

Nenhuma conclusão individual foi escrita pela IA nesta revisão. Fonte didática e assistência técnica estão identificadas no cabeçalho e nas células alteradas.
""")
nb["metadata"]["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("Revisão técnica aplicada; respostas e conclusões individuais não preenchidas.")
