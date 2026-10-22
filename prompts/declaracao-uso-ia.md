# Declaração de Uso de IA

**Nome:** Adrian Michael
**Data:** 22/10/2026
**Disciplina:** Análise e Visualização de Dados (Cesar School, 2026.2)
**Projeto:** Dashboards em Streamlit sobre o Heart Disease Dataset (UCI)

## Ferramenta

- **Claude Code** (CLI da Anthropic), modelo **Claude Sonnet 5.5**.
- Executado localmente, com acesso de leitura e escrita ao repositório e ao terminal.
- Neste projeto não foram usadas outras ferramentas de IA.

## Finalidade do uso

A IA foi usada como assistente de programação para:

1. Analisar o repositório e montar um plano de trabalho (`CHECKLIST.md`, arquivo local não versionado).
2. Implementar os gráficos do Dashboard 1 em `app.py`.
3. Implementar o Dashboard 2 (KPIs) em `app.py` e o cache de dados em `src/data_loader.py`.
4. Organizar os notebooks e redigir esta declaração.

A EDA, o tratamento do dataset (`data/clean/dataset.csv`) e a escolha do tema são do autor. O esqueleto inicial do `app.py` (sidebar, filtros e `TODO`s) e o rascunho `prof_rascunho_dashboard1.png` vieram do repositório-modelo da disciplina. Na análise inicial, o Claude Code leu esse rascunho.

## Prompts usados

Os prompts foram dados em português, em sequência, na mesma sessão:

1. "Analise o repositório, o que deve ser feito no momento, crie um arquivo com um passo a passo e checklist para você se lembrar."
2. "Sim, comece pela Etapa 1." (heatmap de correlação e histograma)
3. "Etapa 2." (cache de dados e conferência de `VARS_QUANT`)
4. "Etapa 3." (Dashboard 2 com KPIs)
5. "Etapa 4." (notebooks e documentação)
6. "Etapa 5." (preparação do deploy e push)
7. "Etapa 6." (revisão final)
8. "Crie uma declaração de Uso de IA profissional e repare que coloquei um rascunho de dashboard, vê se ele serve."

Quando a IA pediu decisões de projeto, o autor respondeu:

- Dashboard 2 na mesma página, abaixo do Dashboard 1, e não em página separada.
- KPIs: total de pacientes, % com doença cardíaca, idade média, colesterol médio e FC máxima média.
- Usar `eda-com-downloads.ipynb` como `eda.ipynb` e remover os notebooks redundantes.
- Repositório público.

## O que foi aceito, modificado ou rejeitado e por quê

### Aceito

- **Heatmap de correlação** (`px.imshow`, escala `RdBu_r` fixa de -1 a 1, valores nas células) e **histograma** (`px.histogram`, colorido por `doenca_cardiaca` quando o toggle está ligado). Seguem os `TODO`s do esqueleto e o rascunho do professor.
- **Tratamento de casos de borda:** avisos para menos de 2 variáveis, nenhuma variável e filtros que deixam poucos ou nenhum paciente. Evita erros do Streamlit com dados vazios.
- **`@st.cache_data` em `load_data`:** evita reler o CSV a cada interação.
- **Cinco KPIs com `st.metric`**, com delta em relação ao dataset completo, para o leitor ver o efeito dos filtros.
- **`width="stretch"`** no lugar de `use_container_width=True`, por este estar depreciado.
- **Consolidação dos notebooks:** `eda-com-downloads.ipynb` virou `eda.ipynb`, conforme a instrução do README.

### Modificado

- O delta do KPI "% com doença cardíaca" usa `delta_color="inverse"` (aumento em vermelho), por ser um indicador de risco. Os demais usam `delta_color="off"`, porque subir ou descer não é bom nem ruim.

### Rejeitado

- **Dashboard 2 em página separada** (`st.navigation`): a página única reaproveita a sidebar e o `df_filtrado` sem duplicar código.
- **Manter os três notebooks:** dois eram redundantes e confundiam a entrega.

## Verificação e responsabilidade

- O código gerado foi executado com o `AppTest` do Streamlit (sem exceções nos cenários: todas as variáveis, toggle ligado, 1 e 0 variáveis, filtros restritivos) e conferido no navegador com `streamlit run app.py`.
- Os valores dos KPIs vistos no app (297 pacientes, 46,1% cardíacos, idade média de 54,5 anos, colesterol de 247 mg/dl e FC máxima de 150 bpm) vêm direto de `data/clean/dataset.csv`.
- O autor revisou o código antes do commit e é responsável pelo conteúdo entregue.
- O trabalho segue o Plano de Ensino quanto à declaração de uso de IA.
