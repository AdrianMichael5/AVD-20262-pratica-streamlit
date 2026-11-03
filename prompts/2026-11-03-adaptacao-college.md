# Assistência de IA — adaptação para College.csv

**Data:** 2026-11-03. **Ferramenta:** Codex (OpenAI). **Responsável:** Adrian Michael.

## Pedido e decisão do autor

Após esclarecer que o notebook original continha a parte individual de College.csv, o autor determinou:

> use college.csv

## Aproveitamento e alterações

- Fonte: o mesmo dataset Kaggle do notebook original; download público de College.csv, sem autenticação. 777 linhas/18 variáveis originais.
- App convertido para College: seleção das 17 quantitativas, correlações, histogramas, filtro Private e comparação institucional. Cinco médias e três gráficos reaproveitam blocos existentes da EDA; a justificativa individual continua pendente.
- Notebook final adaptado do original, que foi preservado intacto. Removidos trechos médicos residuais; tradução de Apps corrigida para candidaturas. Textos/conclusões preexistentes assistidos por Gemini foram identificados como tais, sem novas conclusões pessoais do Codex.
- Transformações Expend_log/Apps_binned preservadas e exportadas; valores originais não truncados, incluindo Grad.Rate = 118. Uso de médias simples, sem ponderação por porte.
- Rascunhos College regenerados, com autoria/data e inspeção visual. Requisitos e documentação atualizados; relatórios médicos marcados como históricos.
- Dois scripts exclusivos da versão médica receberam guarda para não modificar College.

## Verificação

49 células de código executadas sem erros e CSV reproduzido. Dez testes locais aprovados, cobrindo widgets, tipos ausentes, todos os métodos/variáveis, limites, KPIs/deltas e integridade da base. Um problema na limpeza de temporário do teste Windows foi corrigido antes da execução final aprovada.

Evidências: [validação College](../entregas/validacao-college.md), [manifesto](../data/clean/college-manifesto.json) e [execução da EDA](../entregas/execucao-notebook.json).

Não houve publicação, commit/push ou teste de navegador nesta adaptação. Pergunta sobre público/métricas foi encaminhada ao autor; sua justificativa, reflexão, identificação, confirmação de skill e assinatura não foram inventadas.
