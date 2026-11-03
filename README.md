# College — dashboards em Streamlit

Projeto de Adrian Michael para Análise e Visualização de Dados, Cesar School, 2026.2, desenvolvido a partir do modelo da disciplina.

**Tema confirmado pelo autor em 03/11/2026:** College.csv, conforme a EDA do arquivo `Cópia_de_Aula_11_Prática_EDA.ipynb`. A versão atual substitui o app anterior de Heart Disease.

**App publicado:** URL ainda pendente. O projeto College foi enviado ao GitHub em `main`, commit [b1bb1db](https://github.com/AdrianMichael5/AVD-20262-pratica-streamlit/commit/b1bb1db9d8e9c746880180589ee0e36f8f7eb951). O link real do app será incluído após o deploy.

## Dashboards

- **Laboratório:** 17 variáveis quantitativas disponíveis; cinco selecionadas por padrão; correlação Spearman, Pearson ou Kendall; um histograma por variável selecionada.
- **Comparação institucional:** médias de candidaturas recebidas (`Apps`), aceitas (`Accept`), novos matriculados (`Enroll`), gasto educacional por aluno (`Expend`) e taxa de graduação (`Grad.Rate`). Três gráficos: médias por tipo de instituição, dispersão Apps × Accept e boxplot de Expend por tipo.

A sidebar oferece seleção de variáveis, filtro de tipo (`Private`), distinção por cores e intervalos inclusivos. Os filtros afetam as duas abas; retirar uma variável remove seu intervalo. Sem variáveis, permanece apenas o filtro de tipo.

**Público adotado:** coordenação de planejamento institucional, conforme delegação do autor para manter a definição técnica mais adequada à EDA. As cinco variáveis foram reaproveitadas do bloco de médias do notebook original. A [justificativa técnica assistida](entregas/justificativa-metricas.md) foi escrita com Codex e precisa da revisão/justificativa pessoal exigida na atividade.

## Dados e origem

Base obtida da [mesma fonte Kaggle do notebook original](https://www.kaggle.com/datasets/nitishsubandh/dataset). O [site oficial do ISLR](https://www.statlearning.com/resources-second-edition) também disponibiliza College.csv; o [manual do pacote](https://cran.r-project.org/web/packages/ISLR/ISLR.pdf) documenta suas variáveis e o contexto histórico.

- 777 instituições, 18 variáveis de origem; `Expend_log` e `Apps_binned` completam as 20 colunas exportadas.
- As 17 variáveis quantitativas originais ficam disponíveis no laboratório. As duas derivadas não são duplicadas nessa lista.
- As transformações seguem o notebook: logaritmo de `Expend` e tercis de `Apps`, calculados na base completa.
- Nenhuma linha foi excluída e nenhum valor foi truncado. A ocorrência de `Grad.Rate > 100` é preservada e sinalizada no app.
- Métricas são médias simples entre instituições, sem ponderação por alunos; deltas comparam recorte e base completa. Não são indicadores atuais ou comparação entre períodos.

O app lê apenas [data/clean/dataset.csv](data/clean/dataset.csv), sem login Kaggle ou download durante sua execução. O [manifesto](data/clean/college-manifesto.json) registra origem, transformações e hashes.

## Executar

Ambiente validado: Python 3.12.6. Na raiz:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Em macOS/Linux, criar com `python3 -m venv .venv` e ativar com `source .venv/bin/activate`. Depois da ativação, os comandos Python são iguais.

## Reproduzir a EDA e testar

```bash
python -m pip install -r requirements-dev.txt
python scripts/importar_college.py
python scripts/validar_entrega.py notebook
python -m unittest discover -s tests -v
```

O importador usa o cache bruto quando presente; caso contrário baixa a fonte pública. A EDA final já foi executada: **49 células de código sem erros**, exportando **777 linhas e 20 colunas**. **Dez testes locais passaram.** Veja a [validação College](entregas/validacao-college.md).

O arquivo original do autor foi preservado; o notebook final é [notebooks/eda.ipynb](notebooks/eda.ipynb). Nele, a proveniência Gemini dos textos/conclusões preexistentes está explícita; sua revisão individual continua pendente.

## Entregáveis e acompanhamento

- [Checklist e fases](CHECKLIST.md)
- [Changelog com datas, responsáveis e commits anteriores](CHANGELOG.md)
- [Planejamento e dois rascunhos College](entregas/planejamento.md)
- [Orientações das entregas](entregas/README.md)
- [Declaração de IA em PDF, para preencher a reflexão e assinar](prompts/DECLARACAO_IA.pdf)
- [Registro factual em Markdown](prompts/declaracao-uso-ia.md)
- [Roteiro da reflexão individual](prompts/roteiro-reflexao-individual.md)
- [Conferência do template e pendências pessoais](prompts/conferencia-template.md)
- [Preparação da publicação](entregas/preparacao-publicacao.md)
- [Repositório público](https://github.com/AdrianMichael5/AVD-20262-pratica-streamlit) — código College e entregáveis enviados para main.

O PDF foi gerado no template original, com identificação preenchida e campo editável de reflexão. **Antes de assinar:** escrever 8–15 linhas de reflexão, confirmar o uso histórico de `streamlit skills` e revisar as declarações. A assinatura será feita pelo autor; o PDF ainda não está assinado.

`data/raw/`, `.venv/`, `tmp/`, `.env` e `.streamlit/secrets.toml` ficam fora do versionamento. O CSV tratado é intencionalmente versionado para o deploy. Relatórios anteriores de Heart Disease são históricos e não validam o app College.
