# Declaração de Uso de IA

**Nome:** <!-- preencher -->
**Data:** <!-- preencher -->

## Ferramenta

Claude Code (CLI da Anthropic), modelo Claude Sonnet 5.5, com o Streamlit skills instalado no projeto.

## Prompt usado

<!-- Cole aqui o prompt completo que você usou para gerar o esqueleto (ver layout-skeleton-prompt.md), se houver. -->

Pedidos feitos ao Claude Code, em sequência:

1. "Analise o repositório, o que deve ser feito no momento, crie um arquivo com um passo a passo e checklist."
2. "Sim, comece pela Etapa 1" (heatmap de correlação e histograma do Dashboard 1).
3. "Etapa 2" (cache do carregamento de dados e conferência de `VARS_QUANT`).
4. "Etapa 3" (Dashboard 2 com KPIs, na mesma página do `app.py`).
5. "Etapa 4" (organização dos notebooks e documentação).

## O que foi aceito, modificado ou rejeitado e por quê

- **Aceito:**
  - Heatmap com `px.imshow` (escala `RdBu_r` fixa de -1 a 1) e histograma com `px.histogram`, com avisos para filtros sem dados suficientes.
  - `@st.cache_data` em `load_data`, para não reler o CSV a cada interação.
  - Cinco KPIs com `st.metric` (total de pacientes, % com doença cardíaca, idade média, colesterol médio, FC máx. média), com delta em relação ao dataset completo.
  - Troca de `use_container_width=True` por `width="stretch"`, porque o primeiro está depreciado.
- **Modificado:** <!-- ex.: ajustes que você fez depois no código ou no layout -->
- **Rejeitado:**
  - Dashboard 2 em página separada (`st.navigation`): preferi manter tudo no mesmo `app.py`, reaproveitando a sidebar e o `df_filtrado`.
  - Manter três notebooks: o `eda-com-downloads.ipynb` virou o `eda.ipynb`, e o placeholder e o `arquivo-eda-original.ipynb` foram removidos.
