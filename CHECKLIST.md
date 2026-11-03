# Checklist — entrega College.csv

**Atualização:** 2026-11-03, America/Fortaleza. **Responsável:** Adrian Michael.
**Assistência técnica/documental:** Codex (OpenAI). Base Git local: `1c8f1de`; mudanças ainda sem commit.

`[x]` indica evidência local, não aprovação dos testes do app publicado. Ao concluir um item, registrar data, executor, commit e evidência. Resultados anteriores de Heart Disease são históricos.

## Requisitos

| ID | Estado | Requisito / evidência |
| --- | --- | --- |
| E01 | [x] | Tema College.csv confirmado pelo autor; notebook final em `notebooks/eda.ipynb`, adaptado do original preservado. |
| E02 | [x] | EDA com 49 células de código executadas sem erros; exporta as 777 linhas/20 colunas usadas pelo app. Manifesto e hashes registrados. |
| E03 | [ ] | Revisão pessoal das respostas/conclusões preexistentes assistidas por Gemini. Autoria e pendências identificadas no notebook final. |
| S01 | [x] | Seletor com 17 variáveis quantitativas; cinco padrão; teste com todas, uma e nenhuma. |
| S02 | [x] | Slider inclusivo para cada variável selecionada, por interseção; filtro de tipo adicional. Testados os cinco sliders padrão. |
| D01 | [x] | Mapa de correlação Spearman/Pearson/Kendall, escala -1 a 1 e valores nas células. |
| D02 | [x] | Histograma para cada variável avaliada; 17 na seleção completa; toggle por tipo. |
| D03 | [x] | Abas Laboratório e Comparação institucional geradas sem exceção no AppTest. Cliques em navegador do deploy ainda pendentes. |
| D04 | [x] | Público adotado por delegação do autor: coordenação de planejamento institucional. A justificativa técnica assistida está registrada; revisão pessoal segue em A06. |
| D05 | [x] | Cinco métricas implementadas: médias de Apps, Accept, Enroll, Expend e Grad.Rate, reaproveitando o bloco de médias da EDA. A justificativa pessoal é A06. |
| D06 | [x] | Três visuais adicionais no Dashboard 2: médias por tipo, dispersão Apps × Accept e boxplot de Expend por tipo. |
| A01 | [ ] | App, notebook, CSV, src, scripts, testes, entregas e prompts completos no repositório remoto. Os novos arquivos ainda não receberam commit/push. |
| A02 | [x] | Dois rascunhos College em `entregas/`, com autoria/data e identificação de revisão posterior ao app inicial. Conferidos visualmente. |
| A03 | [x] | Repositório público confirmado via GitHub CLI: https://github.com/AdrianMichael5/AVD-20262-pratica-streamlit, branch main. Conteúdo remoto final depende de A01. |
| A04 | [ ] | App publicado e URL real adicionada ao README. |
| A05 | [ ] | PDF `prompts/DECLARACAO_IA.pdf` gerado e conferido em oito páginas, com identificação 5A/Adrian Michael de Araujo/ama3@cesar.school/03-11-2026. Reflexão editável vazia; confirmação de ferramentas/skill, revisão e assinatura pendentes. Entregar também no Classroom. |
| A06 | [ ] | Escolha e justificativa pessoal das métricas/gráficos em `entregas/justificativa-metricas.md`; roteiro atualizado para College, sem respostas inventadas. |
| T01 | [ ] | Abrir a versão publicada em janela anônima e registrar URL/commit/data/executor. |
| T02 | [ ] | Todos os widgets responderem no app publicado. Dez testes locais já aprovados; não substituem este aceite. |
| T03 | [ ] | Clicar nas duas abas no app publicado e conferir os painéis. |
| T04 | [ ] | Revisar exposição de dados no app publicado, arquivos, outputs e histórico. Triagem limitada de credenciais disponível, sem certificação de ausência de vazamento. |

## Desenvolvimento em fases

| Fase | Estado | Evidência / pendência |
| --- | --- | --- |
| 1. Planejamento | Adaptado para College | Dois rascunhos e planejamento; público/justificativa individual pendentes. |
| 2. Implementação | Concluída localmente | App College, cinco KPIs, três gráficos, filtro de tipo e 17 variáveis; dez testes aprovados. |
| 3. Documentação/EDA | Parte técnica realizada | 49 células executadas, CSV conferido e documentação atualizada; textos pessoais e PDF assinado pendentes. |
| 4. Publicação | Preparada | Parâmetros de main/app.py definidos e repositório público; falta commit/push/deploy e URL real. |
| 5. Aceite | Pendente | Executar o roteiro abaixo na versão publicada. |

## Aceite publicado

| Teste | Procedimento / resultado esperado | Estado / evidência |
| --- | --- | --- |
| P01 | URL acessível em janela anônima, sem credenciais do autor ou exceções. | Não executado |
| P02 | Clicar nas duas abas e conferir conteúdo e filtros compartilhados. | Não executado |
| P03 | Selecionar todas, uma e nenhuma variável; verificar histogramas e avisos. | Não executado |
| P04 | Alterar sliders, restringir até zero/um registro quando possível e restaurar; verificar contagem e KPIs. | Não executado |
| P05 | Acionar tipo, toggle, método de correlação e seletor de comparação de médias. | Não executado |
| P06 | Conferir cinco KPIs e três gráficos adicionais com valores do CSV filtrado; médias/deltas e tipos ausentes coerentes. | Não executado |
| P07 | Revisar interface, tooltips, tabelas/downloads se houver e erros; ausência de exposição indevida. | Não executado |
| P08 | Abrir links do README, repositório e entregáveis em janela anônima. | Não executado |

Cada evidência deve incluir URL, commit publicado, data, executor e resultado. Não marcar pela leitura do código.

## Registro atual

Em 2026-11-03, Adrian confirmou “use college.csv”. Codex obteve a mesma base Kaggle do original (777 instituições, 565 Yes/212 No), adaptou o app, o notebook, os rascunhos e os testes. Na validação final, a EDA executou 49 células sem erros em 61,109 s; dez testes locais passaram em 19,390 s. Dados e hashes em [validação College](entregas/validacao-college.md). O original foi preservado; conclusões/declaração Gemini preexistentes permanecem atribuídas e exigem revisão individual.

Histórico de autores/datas/commits e mudanças: [CHANGELOG.md](CHANGELOG.md). Os registros anteriores de Heart Disease não são evidência do app College.
