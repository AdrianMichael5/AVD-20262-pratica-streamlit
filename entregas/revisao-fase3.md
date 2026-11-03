# Histórico — revisão Heart Disease (supersedida)

**Atenção:** o autor confirmou College.csv após esta revisão. Este texto preserva o histórico anterior; a validação atual está em [validacao-college.md](validacao-college.md), e o registro genérico de execução já corresponde a College. As pendências sobre tema descritas abaixo foram resolvidas.

**Data:** 2026-11-03. **Executor:** Codex (OpenAI), solicitado por Adrian Michael.
**Estado:** revisão técnica realizada; conclusão da fase depende das decisões e textos individuais do autor.

## Execução da EDA

- `notebooks/eda.ipynb`: **44 de 44 células de código executadas**, sem erros, em **26,563 segundos**, com Python 3.12.6.
- A execução baixou Heart Disease pela biblioteca `ucimlrepo`, aplicou as transformações existentes e exportou **297 registros e 17 colunas**.
- A exportação foi comparada com o CSV do app por `pandas.testing.assert_frame_equal`, tolerância numérica de `1e-12`; a representação textual anterior foi preservada para evitar alterações de serialização de floats.
- As saídas do notebook foram renovadas, inclusive os gráficos das faixas etárias corrigidas. O kernel salvo tem nome portátil `python3`.
- Registro com hashes: [execucao-notebook.json](execucao-notebook.json).
- Após a reexecução, **os oito testes locais passaram novamente**, em **3,927 segundos**. Isso não substitui teste visual do app ou aceite da versão publicada.

Comandos reproduzíveis, a partir da raiz e com o ambiente ativado:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validar_entrega.py notebook
python -m unittest discover -s tests -v
```

O script de execução exige acesso à UCI e inicia um kernel local. Foram emitidos avisos do ambiente Windows/Jupyter sobre event loop e transporte local do kernel, sem falhas na execução. Os diretórios temporários de renderização e kernel ficam em `tmp/`, ignorado pelo Git.

## Revisão técnica

- Removida a instalação de pacote via `!pip` dentro da EDA; dependências separadas em `requirements-dev.txt`.
- Cabeçalho identifica o material didático de origem e distingue saídas de código de respostas individuais.
- Corrigidas explicações metodológicas sobre cálculo de Pearson, testes por grupo e mecanismo de ausência: não se certifica MCAR/MAR pela simples presença de poucos ausentes.
- Corrigida a descrição de `thal` conforme dicionário da UCI.
- Inseridas marcações `[IA]` nos arquivos assistidos e nas células revisadas. A análise didática original não foi atribuída integralmente ao aluno.
- As respostas às perguntas e a síntese individual não foram preenchidas pela IA.

Fontes técnicas consultadas: [UCI — Heart Disease](https://archive.ics.uci.edu/dataset/45/heart+disease), [SciPy — Pearson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html) e [SciPy — Mann-Whitney](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html). As alterações são de documentação conceitual e execução; não constituem conclusões pessoais sobre os dados.

## Conferência do template de IA

As cinco páginas do PDF local foram extraídas, renderizadas e inspecionadas. Foi constatada a exigência de declaração assinada em **`prompts/DECLARACAO_IA.pdf`**, registro dos usos, marcações de código, justificativa individual das métricas e reflexão de 8–15 linhas.

A [minuta reorganizada nas oito seções](../prompts/declaracao-uso-ia.md) registra os fatos conhecidos e deixa os campos pessoais pendentes. O [histórico anterior](../prompts/historico-declaracao-2026-10-22.md) foi preservado. A [conferência detalhada](../prompts/conferencia-template.md) lista o que falta. Não foi fabricada assinatura, reflexão pessoal ou afirmação de que todos os usos obedeceram às diretrizes.

## Inconsistência de tema a resolver

O notebook local extra `Cópia_de_Aula_11_Prática_EDA.ipynb` tem 124 células e contém trechos finais referentes a **College.csv**, com menção a assistência **Colab AI/Gemini**. O app e o notebook final atual usam **Heart Disease**. O arquivo extra foi preservado, sem copiar suas conclusões para outro tema nem presumir que seja a EDA definitiva.

Foi solicitado ao autor confirmar o tema. Se a entrega deve se basear em College, os dashboards, dados, público e métricas precisam ser adaptados. A execução bem-sucedida de Heart Disease não resolve essa decisão acadêmica.

## Pendências pessoais solicitadas ao autor

1. Tema definitivo: Heart Disease ou College.csv.
2. Turma, nome completo, e-mail e data de entrega; confirmação de uso histórico da skill oficial do Streamlit e das ferramentas pertinentes.
3. Escolha/justificativa individual das métricas e dos gráficos em [justificativa-metricas.md](justificativa-metricas.md).
4. Respostas/síntese individual da EDA e reflexão de 8–15 linhas.
5. Revisão da declaração e assinatura do PDF final.

Publicação, link no README e testes anônimos permanecem nas fases 4 e 5. Nenhuma mudança foi publicada ou commitada nesta fase.
