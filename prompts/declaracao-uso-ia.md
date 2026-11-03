# Declaração de uso de IA — minuta conforme o template

**Atualização:** 2026-11-03. **Estado:** PDF assinado fornecido pelo autor e preservado em [DECLARACAO_IA.pdf](DECLARACAO_IA.pdf). A revisão adicional da EDA foi realizada depois da assinatura e registrada separadamente em [2026-11-03-revisao-final-eda.md](2026-11-03-revisao-final-eda.md), sem modificar o documento assinado.

A conferência do PDF está em [conferencia-template.md](conferencia-template.md). O [histórico anterior](historico-declaracao-2026-10-22.md) foi preservado como relato datado, sem tratá-lo como descrição atual do app.

**Versão atual:** College.csv, confirmado pelo autor com “use college.csv”. Os usos de Heart Disease abaixo são históricos. O app, a EDA, os testes e os rascunhos atuais foram adaptados para College; ver Uso 10. A origem Gemini do notebook fornecido foi incorporada à declaração, sem omitir a geração prévia de textos/conclusões.

## 1. Identificação

| Campo | Informação |
| --- | --- |
| Turma (5A ou 5B) | 5A |
| Nome completo | Adrian Michael de Araujo |
| E-mail | ama3@cesar.school |
| Repositório | https://github.com/AdrianMichael5/AVD-20262-pratica-streamlit |
| Data de entrega | 03/11/2026 |

## 2. Diretrizes e pontos que precisam de revisão

O template reserva ao aluno a escolha e justificativa das métricas, a interpretação dos dados e as conclusões. A assistência de programação e o cálculo podem ser registrados, mas não substituem essas decisões individuais.

**Registro transparente:** o histórico do Claude informa que o layout inicial dos KPIs foi proposto pela IA e aprovado pelo autor. Na sessão Codex, público-alvo, mapeamento de perguntas e os três visuais foram propostos pela IA antes da leitura do PDF. Não serão apresentados como escolhas individuais do aluno. Cabe ao autor revisar a adequação desses usos e escrever sua própria justificativa em [entregas/justificativa-metricas.md](../entregas/justificativa-metricas.md), sem ocultar a assistência anterior.

As perguntas e a síntese pessoal da EDA permanecem pendentes; a revisão técnica não escreveu conclusões em nome do autor.

## 3. Declaração geral

- [x] Houve uso de IA generativa no projeto.
- [ ] O autor revisou o enquadramento de cada uso nas diretrizes e confirmou a versão final.

Esta marcação registra o fato do uso. Não equivale à opção do template que afirma uso **somente nas situações permitidas**, que exige revisão do autor diante dos pontos acima.

## 4. Ferramentas utilizadas

| Ferramenta | Versão / plano | Parte da atividade |
| --- | --- | --- |
| Claude Code (Anthropic) | O histórico de 22/10 informa “Claude Sonnet 5.5”; versão e plano não foram verificados nesta sessão | Implementação inicial, cache, organização dos notebooks e declaração histórica |
| Colab AI / Gemini (conforme o notebook fornecido) | Versão/plano não informados | Adaptação da EDA College, código, textos, conclusões e justificativas preexistentes; revisão individual pendente |
| Codex (OpenAI) | Versão exata/plano não registrados; não inferidos | Auditoria, planejamento, código dos dashboards, testes e revisão documental de 03/11 |
| Skill oficial `streamlit skills` | Codex não a utilizou nesta sessão; uso anterior depende de confirmação do autor | A menção no README-modelo não comprova utilização |

A skill de PDF do ambiente Codex foi usada para conferir o template. Não é a skill oficial do Streamlit. Outras ferramentas históricas eventualmente presentes em notebooks de referência devem ser confirmadas pelo autor antes da declaração final.

## 5. Registro de usos — opção B, blocos por uso relevante

Os arquivos vinculados são registros/resumos; não são apresentados como transcrições completas. Os relatos históricos de outubro ainda dependem da conferência do autor. “Verificação” abaixo identifica quem executou a checagem; não atribui testes da IA ao aluno.

### Uso 1 — diagnóstico e planejamento inicial

- **Data / ferramenta:** 22/10/2026, Claude Code, conforme histórico.
- **Parte:** checklist local inicial e leitura do repositório.
- **Finalidade:** organização do trabalho; enquadramento final a revisar pelo autor.
- **Pedido:** analisar o repositório e criar passo a passo/checklist.
- **Aproveitado / modificado:** plano local mencionado na declaração; arquivo não encontrado no início da auditoria de novembro.
- **Verificação:** relato histórico e commits consultados pelo Codex; o autor deve conferir a sessão original.
- **Registro:** [histórico, prompts por etapa](historico-declaracao-2026-10-22.md).

### Uso 2 — Dashboard 1 e cache

- **Data / ferramenta:** 22/10/2026, Claude Code, conforme histórico.
- **Parte:** `app.py` e `src/data_loader.py`.
- **Finalidade:** sintaxe de gráficos e otimização do carregamento.
- **Pedido:** implementar etapas 1 e 2 conforme esqueleto e rascunho do professor.
- **Aproveitado / modificado:** heatmap, histograma selecionável, avisos e `@st.cache_data`; em novembro o histograma único virou uma grade.
- **Verificação:** o histórico relata AppTest temporário e execução local; os scripts daquela sessão não estão no repositório. A validação de novembro é separada.
- **Registro:** [histórico](historico-declaracao-2026-10-22.md).

### Uso 3 — KPIs iniciais

- **Data / ferramenta:** 22/10/2026, Claude Code, conforme histórico.
- **Parte:** Dashboard 2.
- **Finalidade:** implementação/cálculo de cinco KPIs. A origem da escolha das métricas precisa da revisão individual prevista no template.
- **Pedido:** “Etapa 3”.
- **Aproveitado / modificado:** total, percentual cardíaco, idade, colesterol e FC máxima; deltas comparados à base. Em novembro os deltas ficaram neutros e com unidades explícitas.
- **Verificação:** relato de conferência contra o CSV; testes atuais disponíveis em `tests/test_app.py`.
- **Registro:** [histórico](historico-declaracao-2026-10-22.md).

### Uso 4 — organização, declaração e revisão de código

- **Data / ferramenta:** 22/10/2026, Claude Code, conforme histórico.
- **Parte:** notebooks, declaração e preparação de dependências para deploy.
- **Finalidade:** organização e revisão de código/textos.
- **Pedido:** etapas 4 a 6, declaração profissional e code review.
- **Aproveitado / modificado:** consolidação do notebook, texto histórico e inclusão dos prompts; publicação não realizada. A declaração atual reorganiza o conteúdo pelos campos do template.
- **Verificação:** commits `81c9483`, `d35be7b`, `5565440`, `1c8f1de` e relato anterior; revisão do autor pendente.
- **Registro:** [histórico](historico-declaracao-2026-10-22.md).

### Uso 5 — auditoria dos requisitos

- **Data / ferramenta:** 03/11/2026, Codex.
- **Parte:** checklist, changelog e README.
- **Finalidade:** comparar os arquivos com o enunciado e documentar pendências.
- **Pedido:** analisar o que existe/falta e criar checklist e changelog com datas/autores.
- **Aproveitado / modificado:** diagnóstico, histórico reconstruído dos commits e roteiro de aceite.
- **Verificação:** leitura estática, contagem do CSV, histórico Git e links relativos pelo Codex.
- **Registro:** [auditoria](2026-11-03-auditoria-entrega.md).

### Uso 6 — planejamento e rascunhos

- **Data / ferramenta:** 03/11/2026, Codex.
- **Parte:** `entregas/planejamento.md`, rascunhos e script de desenho.
- **Finalidade:** layout; houve também proposta de público/visuais pela IA, que não é atribuída ao aluno e exige revisão das diretrizes.
- **Pedido:** “comece”, após a apresentação das cinco fases.
- **Aproveitado / modificado:** proposta de coordenação de pesquisa em cardiologia, perguntas, fórmulas e dois PNGs; decisões pessoais ainda não documentadas pelo autor.
- **Verificação:** PNGs inspecionados visualmente pelo Codex. Gráficos esquemáticos, sem dados; rascunhos posteriores ao app inicial.
- **Registro:** [fase 1](2026-11-03-fase1-planejamento.md).

### Uso 7 — implementação e testes

- **Data / ferramenta:** 03/11/2026, Codex.
- **Parte:** app, agregações, teste, notebook e coluna etária do CSV.
- **Finalidade:** sintaxe/cálculos e depuração; não substitui a justificativa pessoal das escolhas de métricas/gráficos.
- **Pedido:** “Continue”.
- **Aproveitado / modificado:** duas abas, histogramas por variável, três gráficos, filtros comuns e rótulos etários corrigidos; demais valores do CSV preservados.
- **Verificação:** oito testes locais executados pelo Codex, com resultado em [validação da fase 2](../entregas/validacao-fase2.md).
- **Registro:** [fase 2](2026-11-03-fase2-implementacao.md).

### Uso 8 — revisão técnica/documental

- **Data / ferramenta:** 03/11/2026, Codex.
- **Parte:** EDA, marcações `[IA]`, declaração e documentação.
- **Finalidade:** execução/depuração técnica, conferência do template e organização factual do registro.
- **Pedido:** “faça”, em resposta à proposta da fase 3.
- **Aproveitado / modificado:** distinção entre material didático e produção individual, revisão conceitual de premissas estatísticas com fontes, remoção de instalação de pacote dentro do notebook e preparação dos campos da declaração.
- **Verificação:** cinco páginas do template extraídas/renderizadas e inspecionadas; execução da EDA e verificações técnicas registradas no relatório da fase 3, conforme resultado efetivo.
- **Registro:** [fase 3](2026-11-03-fase3-documentacao.md).

### Uso 9 — preparação da publicação

- **Data / ferramenta:** 03/11/2026, Codex.
- **Parte:** revisão dos arquivos/histórico, ambiente local e documentação de deploy.
- **Finalidade:** conferência técnica e depuração do ambiente; sem publicação.
- **Pedido:** novo “continue” após a revisão da fase 3.
- **Aproveitado / modificado:** script de triagem de credenciais, consulta ao GitHub e parâmetros preparados para deploy. Nenhum commit/push realizado.
- **Verificação:** GitHub CLI confirmou repositório público e commit remoto; triagem sem achados nos padrões pesquisados; servidor local respondeu HTTP 200/`ok`. A inspeção visual foi tentada com a skill de controle do computador, mas o host estava indisponível. Essa skill não é a skill oficial do Streamlit.
- **Registro:** [fase 4](2026-11-03-fase4-preparacao.md) e [preparação da publicação](../entregas/preparacao-publicacao.md). Não houve teste anônimo ou conclusão das partes pessoais pendentes.

### Uso 10 — conversão para College.csv

- **Data / ferramenta:** 03/11/2026, Codex; notebook original declara assistência anterior de Colab AI/Gemini.
- **Parte:** app, notebook final, CSV, agregações, testes, rascunhos e documentação.
- **Finalidade:** adaptação técnica ao tema escolhido pelo autor, sintaxe e reprodução dos blocos já existentes. Não substitui decisão e justificativa individual das métricas.
- **Pedido:** “use college.csv”.
- **Aproveitado / modificado:** cinco variáveis do bloco de médias, dispersão Apps × Accept e boxplot por Private; 17 quantitativas no laboratório. Dados obtidos da mesma fonte Kaggle e transformações preservadas. Trechos médicos removidos da cópia final; original intacto. Textos/conclusões Gemini preexistentes mantidos com atribuição e revisão pessoal pendente.
- **Verificação:** 49 células executadas sem erros, exportação conferida e dez testes locais aprovados; rascunhos inspecionados visualmente. Resultados em [validacao-college.md](../entregas/validacao-college.md). Sem teste visual do app ou publicação.
- **Registro:** [adaptação College](2026-11-03-adaptacao-college.md).

### Uso 11 — definição técnica, identificação, PDF e envio ao GitHub

- **Data / ferramenta:** 03/11/2026, Codex.
- **Parte:** justificativa técnica, declaração/PDF, documentação e versionamento.
- **Finalidade:** organizar a proposta técnica solicitada e os registros objetivos; não escrever reflexão pessoal ou assinar pelo aluno.
- **Pedido:** “Faça oque fizer mais sentido”; dados da turma 5A e identificação fornecidos; “Gere o PDF e eu assino”; publicar app e “commite tudo e faz push”.
- **Aproveitado / modificado:** mantidas as cinco comparações existentes da EDA para planejamento institucional; justificativa técnica com autoria de IA explícita. Identificação preenchida e PDF gerado no template original, com anexos e reflexão editável. O autor escreverá sua reflexão e assinará.
- **Verificação:** PDF renderizado e inspecionado; campo da reflexão conferido também na árvore AcroForm, sem conteúdo inventado. Commit/push autorizados; resultado registrado no Git e na documentação após a execução. A ferramenta de acesso ao navegador está indisponível; não há URL pública confirmada do app.
- **Registro:** [roteiro da reflexão](roteiro-reflexao-individual.md) e histórico Git/CHANGELOG.

### Uso 12 — redação assistida da reflexão

- **Data / ferramenta:** 03/11/2026, Codex.
- **Parte:** seção 7, arquivo de texto da reflexão e campo correspondente do PDF.
- **Finalidade:** redigir em tom direto a partir dos fatos e relatos fornecidos pelo autor, que solicitou salvar e commitar. Não se apresenta a redação como produção sem assistência de IA.
- **Aproveitado / modificado:** texto em dez linhas, mencionando a decisão College, a revisão das métricas e os testes que o autor declarou ter realizado. Revisão e assinatura permanecem pessoais.
- **Verificação:** texto conferido no Markdown, no valor do campo AcroForm e na renderização do PDF; assinatura não inserida.
- **Registro:** [reflexao-individual.txt](reflexao-individual.txt), seção 7 e histórico Git.

## 6. Trechos de código feitos com apoio de IA

| Arquivo / parte | Apoio de IA | Tipo de apoio |
| --- | --- | --- |
| `app.py`, estrutura atual | Sim | Claude na implementação inicial; Codex na reorganização por abas e filtros |
| Dashboard 1 | Sim | Heatmap/histogramas, labels e tratamento de estados |
| Dashboard 2 | Sim | Implementação, agregações e proposta de visuais; escolha/justificativa individual pendente |
| `src/data_loader.py` | Sim | Cache histórico Claude; adaptação Codex para College com caminho independente do diretório |
| `src/analysis.py`, `tests/`, `scripts/`, script dos rascunhos | Sim | Cálculos, testes, migração, execução e desenho por Codex |
| `notebooks/eda.ipynb` | Sim | Notebook College fornecido declara Gemini em código/textos/conclusões; integração técnica/reprodução por Codex. Revisão individual das conclusões e justificativas pendente |
| Deploy/configuração | Sem deploy nesta sessão | Preparação relatada anteriormente; publicação e teste externo pendentes |

Marcações `# [IA] ferramenta - finalidade` identificam arquivos inteiramente assistidos e células alteradas. A ausência de marcação em material didático não é certificação de autoria própria.

## 7. Reflexão individual — 8 a 15 linhas

**Redação com apoio do Codex, solicitada pelo autor e baseada nos seus relatos.** O texto está em [reflexao-individual.txt](reflexao-individual.txt) e no campo editável do PDF. O autor deve revisá-lo antes de assinar; esta assistência está registrada no Uso 12.

Usei a IA para me ajudar a transformar a EDA do College.csv em um app no Streamlit.

Ela ajudou no código, nos gráficos, nos filtros, nos testes e na documentação.

No começo, o projeto usava Heart Disease, então pedi a mudança para College.csv.

Fiz isso porque College era a base do meu notebook e precisava aparecer no app.

Analisei a justificativa das métricas e a proposta de planejamento institucional.

Foram usadas médias de candidaturas, aceitações, matrículas, gastos e graduação.

Testei o app publicado para conferir o funcionamento dos painéis e dos filtros.

Os testes automatizados também ajudaram a conferir os cálculos do projeto.

Os dados são históricos e valores como graduação acima de 100% exigem cuidado.

A IA ajudou no desenvolvimento, mas revisar e entender a entrega é minha responsabilidade.

## 8. Termo de responsabilidade

O termo do template deve ser lido e confirmado pessoalmente pelo autor, que precisa compreender e explicar código, saídas e análises. Não foi assinado ou declarado verdadeiro pela IA em nome do aluno.

**Nome completo:** Adrian Michael de Araujo.

**Assinatura:** arquivo assinado fornecido pelo autor; presença estrutural conferida e bytes preservados. Não foi realizada validação criptográfica externa.

**Data:** 03/11/2026.

O autor confirmou a entrega no Classroom. Este Markdown guarda a preparação histórica e os registros complementares; não altera ou amplia retroativamente o conteúdo coberto pela assinatura do PDF.
