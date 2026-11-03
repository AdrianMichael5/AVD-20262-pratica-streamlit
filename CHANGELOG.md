# Changelog

Registro de mudanças relevantes, organizado por categorias no estilo Keep a Changelog. Datas em `AAAA-MM-DD`. O projeto ainda não tem uma versão de entrega identificada neste registro; as datas históricas abaixo agrupam commits, não releases publicadas.

O Git é a fonte de autoria e detalhe técnico. Cada entrada deve indicar o que mudou, a data, o responsável e o commit ou a evidência correspondente. Para novos commits, recomenda-se o formato `tipo(escopo): descrição`, por exemplo `docs(entrega): atualiza checklist de aceite`.

## [Não lançado]

**Tema atual:** College.csv, confirmado pelo autor em 2026-11-03. As entradas de Heart Disease abaixo registram a implementação anterior, supersedida; não validam o app atual.

### Adaptação para College — 2026-11-03

- **2026-11-03 — Codex (OpenAI), solicitado por Adrian Michael de Araujo:** identificação preenchida com dados fornecidos, proposta técnica de métricas mantida por delegação do autor e roteiro da reflexão criado. PDF gerado no template original, com anexos de usos, campo AcroForm de reflexão e assinatura pendente; oito páginas renderizadas e conferidas. Autor solicitou commit e push de todos os arquivos; publicação Streamlit depende do painel web, indisponível por esta sessão.

- **Responsável:** Adrian Michael; **implementação/revisão assistida:** Codex (OpenAI). Pedido explícito: “use college.csv”.
- Substituídos dados e notebook final pela EDA College fornecida, preservando o arquivo original. Download da mesma fonte Kaggle: 777 instituições, 18 variáveis originais, duas derivadas; manifesto com hashes e transformações.
- App com 17 variáveis quantitativas, filtro Private, histogramas por variável e Spearman/Pearson/Kendall. Dashboard 2 com cinco médias e três visuais reaproveitados dos blocos da EDA, com justificativa individual pendente.
- Atualizados rascunhos, checklist, README, planejamento e declaração; assistência Gemini original e textos/conclusões preexistentes mantidos com atribuição e revisão pessoal pendente.
- Carregamento do CSV independente do diretório atual; dependências de notebook separadas das do app. Scripts médicos históricos protegidos contra alteração de College.
- CSV/notebook/JSON padronizados em LF e `.gitattributes` adicionado para preservar hashes entre Windows e Linux; marcações de IA completadas no código integrado do notebook.
- **Validação atual:** 49 células de código sem erros em 61,109 s, CSV reproduzido (777 × 20); dez testes locais aprovados em 19,390 s. PNGs dos dois rascunhos inspecionados. Detalhes em `entregas/validacao-college.md`. Sem commit/push/deploy ou teste visual do app. Demais pendências pessoais/assinatura mantidas.

### Adicionado

- **2026-11-03 — Codex (OpenAI), a pedido de Adrian Michael, preparação da fase 4:** script `scripts/auditar_publicacao.py`, resultado da triagem e `entregas/preparacao-publicacao.md`, com consulta ao GitHub, parâmetros de deploy e teste HTTP local.

- **2026-11-03 — Codex (OpenAI), a pedido de Adrian Michael, fase 3:** `requirements-dev.txt`, scripts de revisão/execução da EDA, registro de execução com hashes e relatório `entregas/revisao-fase3.md`; conferência das cinco páginas do template, histórico preservado da declaração anterior e roteiro `entregas/justificativa-metricas.md` sem respostas pessoais.

- **2026-11-03 — Codex (OpenAI), a pedido de Adrian Michael, fase 2:** três gráficos no perfil da amostra (classe, percentual cardíaco por faixa etária e colesterol por classe), agregações em `src/analysis.py`, oito testes locais em `tests/test_app.py`, script de correção etária e relatório `entregas/validacao-fase2.md`.

- **2026-11-03 — Codex (OpenAI), a pedido de Adrian Michael, fase 1:** `entregas/planejamento.md`, com público-alvo, perguntas, cinco KPIs, três visuais, regras de filtros e estados vazios; dois rascunhos PNG e `entregas/gerar-rascunhos.ps1` para reprodução. Rascunhos identificados como revisão posterior ao app inicial; ambos inspecionados visualmente. Sem alteração funcional nesta fase.

- **2026-11-03 — Codex (OpenAI), a pedido de Adrian Michael:** `CHECKLIST.md` com diagnóstico dos requisitos, pendências, responsáveis, critérios de conclusão e roteiro de aceite do app publicado.
- **2026-11-03 — Codex (OpenAI), a pedido de Adrian Michael:** este `CHANGELOG.md`, com reconstrução do histórico local a partir dos commits existentes.
- **2026-11-03 — Codex (OpenAI), a pedido de Adrian Michael:** `entregas/README.md` com orientação para os dois rascunhos e evidências. Os rascunhos não foram produzidos nesta revisão.
- **2026-11-03 — Codex (OpenAI), a pedido de Adrian Michael:** `prompts/2026-11-03-auditoria-entrega.md`, registrando o pedido e a assistência documental desta sessão.

### Alterado

- **2026-11-03 — Codex (OpenAI), preparação da fase 4:** README/checklist/declaração com repositório público confirmado, remoto ainda sem melhorias e publicação pendente. Triagem de 31 blobs históricos e arquivos locais sem achados nos padrões pesquisados; servidor em loopback respondeu HTTP 200/`ok`. Inspeção visual não realizada por indisponibilidade do host de navegador.

- **2026-11-03 — Codex (OpenAI), fase 3:** EDA com fonte didática identificada, dependências fora do kernel, ajustes conceituais referenciados e 44 células de código reexecutadas; oito testes locais aprovados novamente. Declaração reorganizada nas oito seções do template, marcações `[IA]` nos arquivos assistidos e documentação atualizada. Tema definitivo e participação Gemini/skill no histórico solicitados ao autor após encontrar trechos College.csv no notebook extra.

- **2026-11-03 — Codex (OpenAI), fase 2:** `app.py` com abas Laboratório/Perfil da amostra, histograma para cada variável selecionada, público-alvo explícito, rótulos/unidades e cores de classe consistentes; deltas neutros em relação à base completa. Filtros compartilhados e avisos para seleção/amostra vazia ou correlação indefinida. README, checklist e declaração de IA atualizados.

- **2026-11-03 — Codex (OpenAI), fase 1:** checklist com acompanhamento explícito das cinco fases e rascunhos concluídos; README, orientações de entregas e declaração de IA atualizados. Registrada pendência D07: os rótulos etários da EDA/CSV divergem dos limites do `pd.cut`; correção planejada para a fase 2.

- **2026-11-03 — Codex (OpenAI), a pedido de Adrian Michael:** README com links para checklist, changelog e entregas, e indicação de publicação ainda não comprovada; declaração de IA com adendo sobre a sessão atual.

### Corrigido

- **2026-11-03 — Codex (OpenAI), fase 2:** rótulos de `faixa_etaria` no notebook e no CSV alinhados aos limites originais inclusivos à direita; demais valores preservados. Saídas do notebook a partir da célula alterada limpas para não apresentar gráficos antigos como atualizados.

**Validação:** fase 2 com oito testes aprovados em 6,120 s; fase 3 com 44 células executadas sem erros em 26,563 s, CSV reproduzido (297 registros/17 colunas) e oito testes aprovados novamente em 3,927 s. Relatórios em `entregas/validacao-fase2.md` e `entregas/revisao-fase3.md`. Testes em navegador/publicação pendentes. A fase 3 depende de tema, textos/decisões pessoais e PDF assinado. Mudanças ainda sem commit no momento da redação.

## 2026-10-22 — implementação e declaração de IA

### Adicionado / alterado

- **AdrianMichael5 — `81c9483`:** implementação dos dashboards de distribuição/correlação e cinco KPIs em página única, cache de carregamento e notebook final, conforme histórico e arquivos resultantes.
- **AdrianMichael5 — `d35be7b`:** declaração de uso de IA.
- **AdrianMichael5 — `5565440`:** detalhamento dos prompts por etapa na declaração.
- **AdrianMichael5 — `1c8f1de`:** registro da revisão de código e correções na declaração.

**Origem:** histórico Git local. A declaração atribui assistência de implementação ao Claude Code; os nomes acima são os autores dos commits. Os testes locais ali relatados não foram reexecutados nesta auditoria. Não há comprovação de deploy associada a essas entradas.

## 2026-10-21 — base da disciplina

### Adicionado

- **Maira Lira — `c62060b`:** commit inicial.
- **Maira Lira — `bfba087`:** instruções iniciais do repositório-modelo.
- **Maira Lira — `71fb85b`:** importação da EDA e arquivos de dados.
- **Maira Lira — `e811fba`:** primeiro rascunho de dashboard.

**Origem:** autores, datas e mensagens do histórico Git local. Essas entradas registram a base da disciplina, sem atribuí-la ao aluno ou à assistência atual.

## Convenção de manutenção

- Manter mudanças ainda não entregues em **Não lançado**. Ao entregar uma versão, criar seção com versão/tag real e data, sem inventar uma publicação retroativa.
- Usar categorias como **Adicionado**, **Alterado**, **Corrigido**, **Removido** e **Segurança**, apenas quando aplicáveis.
- Registrar autor humano e assistência de IA separadamente; a responsabilidade pela entrega permanece com o autor.
- Para comprovar autoria, data e conteúdo exatos, consultar `git log` e `git show <commit>`. Resultado de testes deve apontar para uma evidência, não ser inferido do commit.
