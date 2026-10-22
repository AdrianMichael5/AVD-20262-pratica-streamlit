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

A interação foi conduzida em português, em uma única sessão, em **etapas sequenciais**. As mensagens enviadas eram curtas e estão transcritas abaixo da tabela. A tabela é um **resumo** do que cada etapa pedia e do contexto que a IA leu no repositório (README, `TODO`s e rascunho do professor).

| Etapa | Objetivo do pedido | Contexto e restrições (lidos pela IA no repositório) | Resultado esperado |
| --- | --- | --- | --- |
| 0 | Diagnosticar o repositório e planejar o trabalho | Repositório-modelo da disciplina, com `TODO`s no `app.py` e no `data_loader.py` | Plano com passo a passo e checklist, salvo em arquivo local |
| 1 | Implementar o Dashboard 1 | Seguir o esqueleto e o rascunho do professor; Plotly; dados só via `src/data_loader.py` | Heatmap de correlação e histograma, com tratamento de filtros vazios |
| 2 | Otimizar o carregamento de dados | Manter a interface de `load_data` | `@st.cache_data` e conferência de `VARS_QUANT` com a EDA |
| 3 | Implementar o Dashboard 2 | KPIs na mesma página, reaproveitando sidebar e `df_filtrado` | Cinco KPIs com `st.metric` e delta contra o dataset completo |
| 4 | Organizar a documentação e os notebooks | README como referência de entregáveis | Notebook final como `eda.ipynb` e rascunho desta declaração |
| 5 | Preparar o deploy | Streamlit Community Cloud; repositório público | Verificação de `requirements.txt` e de `data/clean/`; commit e push. **O deploy em si ainda não foi feito** |
| 6 | Revisão final | Checklist do README | Lista do que ainda dependia do autor |
| 7 | Redigir esta declaração e revisar o código | Requisitos do `prompts/README.md` | Declaração e `/code-review` em nível alto (ver seção própria) |

Mensagens originais, em ordem:

1. "Analise o repositório, o que deve ser feito no momento, crie um arquivo com um passo a passo e checklist para você se lembrar."
2. "Sim, comece pela Etapa 1."
3. "Etapa 2."
4. "Etapa 3."
5. "Etapa 4."
6. "Etapa 5."
7. "Etapa 6."
8. "Crie uma declaração de Uso de IA profissional e repare que coloquei um rascunho de dashboard, vê se ele serve."
9. Pedido para rodar um code review do código (ver "Revisão de código").

O arquivo `layout-skeleton-prompt.md` não foi preenchido, e **não houve rascunho do Dashboard 2**: o layout dos KPIs foi proposto pela IA e aprovado pelo autor. O rascunho do Dashboard 1 usado como referência foi o do professor.

Quando a IA apresentou alternativas, as decisões foram do autor:

- Dashboard 2 na mesma página, abaixo do Dashboard 1, e não em página separada.
- KPIs: total de pacientes, % com doença cardíaca, idade média, colesterol médio e FC máxima média.
- `eda-com-downloads.ipynb` como `eda.ipynb`, removendo os notebooks redundantes.
- Repositório público.

## O que foi aceito, modificado ou rejeitado e por quê

### Aceito

- **Heatmap de correlação** (`px.imshow`, escala `RdBu_r` fixa de -1 a 1, valores nas células) e **histograma** (`px.histogram`, colorido por `doenca_cardiaca` quando o toggle está ligado). Seguem os `TODO`s do esqueleto e o rascunho do professor.
- **Tratamento de casos de borda:** avisos para menos de 2 variáveis, nenhuma variável e filtros que deixam poucos ou nenhum paciente. Evita erros do Streamlit com dados vazios.
- **`@st.cache_data` em `load_data`:** evita reler o CSV a cada interação.
- **Cinco KPIs com `st.metric`**, com delta em relação ao dataset completo, para o leitor ver o efeito dos filtros. O delta de "% com doença cardíaca" usa `delta_color="inverse"` (aumento em vermelho, por ser indicador de risco) e os demais usam `"off"`.
- **`width="stretch"`** no lugar de `use_container_width=True`, por este estar depreciado.
- **Consolidação dos notebooks:** `eda-com-downloads.ipynb` virou `eda.ipynb`, conforme a instrução do README.

### Modificado

- Nenhuma edição manual do código gerado pela IA foi registrada até a data desta declaração.

### Rejeitado

- **Dashboard 2 em página separada** (`st.navigation`): a página única reaproveita a sidebar e o `df_filtrado` sem duplicar código.
- **Manter os três notebooks:** dois eram redundantes e confundiam a entrega.

## Revisão de código

Ao final, foi executado o `/code-review` do Claude Code em nível alto sobre o repositório. A revisão apontou, em síntese:

- Esta declaração resumia os prompts em vez de registrá-los. Foram acrescentadas as mensagens originais.
- O delta dos KPIs estava listado como "Modificado", embora fosse a implementação inicial da IA. Foi movido para "Aceito".
- A declaração não dizia que o Dashboard 2 não teve rascunho, que o deploy não foi feito e que o `layout-skeleton-prompt.md` não foi usado. Isso foi acrescentado.
- As afirmações de verificação não tinham evidência versionada. O texto abaixo foi ajustado para dizer exatamente o que foi feito.

O código do app (`app.py` e `src/data_loader.py`) não teve defeitos apontados.

## Verificação e responsabilidade

- Durante a sessão, a IA executou o app com o `AppTest` do Streamlit (todas as variáveis, toggle ligado, 1 e 0 variáveis, filtros restritivos) e não houve exceções. Esses scripts eram temporários e **não estão versionados**.
- O app foi executado localmente com `streamlit run app.py`.
- Os valores dos KPIs sem filtro (297 pacientes, 46,1% cardíacos, idade média de 54,5 anos, colesterol de 247 mg/dl e FC máxima de 150 bpm) vêm de `data/clean/dataset.csv` e foram conferidos contra o arquivo.
- O autor é responsável pelo conteúdo entregue.
