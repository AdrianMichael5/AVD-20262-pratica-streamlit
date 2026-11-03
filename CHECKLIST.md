# Checklist — entrega College.csv

**Atualização:** 2026-11-03, America/Fortaleza. **Responsável:** Adrian Michael.
**Assistência técnica/documental:** Codex (OpenAI). Base histórica: `1c8f1de`; entrega College enviada a main no commit `b1bb1db`, após autorização expressa do autor.

`[x]` indica evidência local, não aprovação dos testes do app publicado. Ao concluir um item, registrar data, executor, commit e evidência. Resultados anteriores de Heart Disease são históricos.

## Requisitos

| ID | Estado | Requisito / evidência |
| --- | --- | --- |
| E01 | [x] | Tema College.csv confirmado pelo autor; notebook final em `notebooks/eda.ipynb`, adaptado do original preservado. |
| E02 | [x] | EDA final com 50 células de código sem erros, CSV de 777 linhas/20 colunas reproduzido e 12 testes aprovados. Evidências em `entregas/revisao-final-eda.md`. |
| E03 | [x] | Revisão assistida concluída a pedido do autor: respostas/conclusões conferidas contra resultados, resíduos médicos e afirmações não sustentadas corrigidos. Autoria Codex explícita; não certifica análise independente do aluno. |
| S01 | [x] | Seletor com 17 variáveis quantitativas; cinco padrão; teste com todas, uma e nenhuma. |
| S02 | [x] | Slider inclusivo para cada variável selecionada, por interseção; filtro de tipo adicional. Testados os cinco sliders padrão. |
| D01 | [x] | Mapa de correlação Spearman/Pearson/Kendall, escala -1 a 1 e valores nas células. |
| D02 | [x] | Histograma para cada variável avaliada; 17 na seleção completa; toggle por tipo. |
| D03 | [x] | Abas Laboratório e Comparação institucional geradas sem exceção no AppTest. Cliques em navegador do deploy ainda pendentes. |
| D04 | [x] | Público adotado por delegação do autor: coordenação de planejamento institucional. A justificativa técnica assistida está registrada; revisão pessoal segue em A06. |
| D05 | [x] | Cinco métricas implementadas: médias de Apps, Accept, Enroll, Expend e Grad.Rate, reaproveitando o bloco de médias da EDA. A justificativa pessoal é A06. |
| D06 | [x] | Três visuais adicionais no Dashboard 2: médias por tipo, dispersão Apps × Accept e boxplot de Expend por tipo. |
| A01 | [x] | App, notebook, CSV, src, scripts, testes, entregas e prompts enviados ao repositório remoto em `b1bb1db`; notebook original e PDF de template incluídos conforme pedido “commite tudo”. Segredos/ambiente/temporários ignorados. |
| A02 | [x] | Dois rascunhos College em `entregas/`, com autoria/data e identificação de revisão posterior ao app inicial. Conferidos visualmente. |
| A03 | [x] | Repositório público confirmado via GitHub CLI: https://github.com/AdrianMichael5/AVD-20262-pratica-streamlit, branch main. Conteúdo remoto final depende de A01. |
| A04 | [x] | URL de publicação informada pelo autor e adicionada ao README: https://college-adrian-avd.streamlit.app/. Resposta HTTP 200 em 03/11/2026; aceite funcional publicado continua em T01–T04. |
| A05 | [x] | PDF assinado fornecido pelo autor, copiado sem alterações para `prompts/DECLARACAO_IA.pdf`; presença estrutural de assinatura e igualdade SHA256 conferidas. Autor confirmou entrega no Classroom; validação criptográfica externa não executada. Revisão adicional da EDA registrada separadamente após a assinatura. |
| A06 | [x] | Revisão confirmada pelo autor: “Analisei o justificativa métricas”. O próprio autor marcou os itens de revisão no arquivo; registro de autoria preservado, sem verificação independente de compreensão pela IA. |
| T01 | [x] | Autor confirmou o item de teste publicado em janela anônima com “Está testado”, em 03/11/2026. URL: https://college-adrian-avd.streamlit.app/. Commit efetivamente testado não informado. |
| T02 | [x] | Testes dos widgets confirmados pelo autor no relato geral; sem detalhamento individual de casos. Dez testes locais já disponíveis como evidência técnica separada. |
| T03 | [x] | Testes das duas abas confirmados pelo autor no relato geral do item 1. Não executados em navegador pela IA. |
| T04 | [x] | Revisão de exposição no app incluída no item de testes que o autor declarou concluído. Complementada pela triagem limitada local anterior; não constitui certificação de segurança. |

## Desenvolvimento em fases

| Fase | Estado | Evidência / pendência |
| --- | --- | --- |
| 1. Planejamento | Registrado e revisado pelo autor | Dois rascunhos, público adotado por delegação e revisão da justificativa confirmada pelo autor. Autoria assistida declarada. |
| 2. Implementação | Concluída localmente | App College, cinco KPIs, três gráficos, filtro de tipo e 17 variáveis; testes locais aprovados. |
| 3. Documentação/EDA | Revisão assistida concluída | 50 células executadas, CSV reproduzido e 12 testes aprovados; PDF assinado preservado, Classroom confirmado pelo autor. |
| 4. Publicação | URL registrada; aceite pendente | Código enviado a main; autor informou https://college-adrian-avd.streamlit.app/, incluída no README. HTTP 200 verificado; carregamento completo no navegador ainda não validado. |
| 5. Aceite | Teste geral confirmado pelo autor | Relato “Está testado”, em 03/11/2026. Não houve execução independente pela IA nem detalhamento de todos os casos do roteiro abaixo. |

## Aceite publicado

| Teste | Procedimento / resultado esperado | Estado / evidência |
| --- | --- | --- |
| P01 | URL acessível em janela anônima, sem credenciais do autor ou exceções. | Confirmado no relato geral do autor; caso sem detalhamento |
| P02 | Clicar nas duas abas e conferir conteúdo e filtros compartilhados. | Confirmado no relato geral do autor; caso sem detalhamento |
| P03 | Selecionar todas, uma e nenhuma variável; verificar histogramas e avisos. | Confirmado no relato geral do autor; caso sem detalhamento |
| P04 | Alterar sliders, restringir até zero/um registro quando possível e restaurar; verificar contagem e KPIs. | Confirmado no relato geral do autor; caso sem detalhamento |
| P05 | Acionar tipo, toggle, método de correlação e seletor de comparação de médias. | Confirmado no relato geral do autor; caso sem detalhamento |
| P06 | Conferir cinco KPIs e três gráficos adicionais com valores do CSV filtrado; médias/deltas e tipos ausentes coerentes. | Confirmado no relato geral do autor; caso sem detalhamento |
| P07 | Revisar interface, tooltips, tabelas/downloads se houver e erros; ausência de exposição indevida. | Confirmado no relato geral do autor; caso sem detalhamento |
| P08 | Abrir links do README, repositório e entregáveis em janela anônima. | Não informado |

O autor confirmou a conclusão geral dos testes publicados em 03/11/2026. A coluna acima registra o relato geral, sem atribuir ao autor evidências por caso que ele não forneceu. A IA não executou esses testes em navegador. O relato geral é registrado em T01–T04. P08 e a identificação exata do commit testado não foram detalhados.

Para novas evidências, registrar URL, commit publicado, data, executor e resultado. Não marcar pela leitura do código.

## Registro atual

Em 2026-11-03, Adrian confirmou “use college.csv”. Codex obteve a mesma base Kaggle do original (777 instituições, 565 Yes/212 No), adaptou o app, o notebook, os rascunhos e os testes. Na validação final, a EDA executou 49 células sem erros em 61,109 s; dez testes locais passaram em 19,390 s. Dados e hashes em [validação College](entregas/validacao-college.md). O original foi preservado; conclusões/declaração Gemini preexistentes permanecem atribuídas e exigem revisão individual.

Revisão final de 03/11/2026: o autor solicitou a conclusão da EDA pelo Codex, forneceu o PDF assinado e confirmou Classroom. Resultados, correções e limites em [entregas/revisao-final-eda.md](entregas/revisao-final-eda.md). O PDF assinado não foi alterado; assistência posterior registrada em documento separado.

Histórico de autores/datas/commits e mudanças: [CHANGELOG.md](CHANGELOG.md). Os registros anteriores de Heart Disease não são evidência do app College. O checklist registra evidências técnicas/relatos, sem certificar avaliação acadêmica ou autoria independente.
