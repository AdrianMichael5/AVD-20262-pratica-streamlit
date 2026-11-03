# Preparação da publicação — College.csv

**Data:** 2026-11-03. **Executor:** Codex (OpenAI), solicitado por Adrian Michael.
**Estado:** sem commit/push/deploy; URL pública ainda pendente.

## Parâmetros

| Campo | Valor |
| --- | --- |
| Repositório público confirmado | AdrianMichael5/AVD-20262-pratica-streamlit |
| Branch | main |
| Entrada | app.py |
| Python validado | 3.12.6; linha 3.12 para deploy |
| Dependências do app | requirements.txt |
| Dados usados pelo app | data/clean/dataset.csv, College, 777 linhas/20 colunas |
| Autenticação/segredos do app | Nenhum; não baixa da Kaggle em execução |
| Versão remota consultada | 1c8f1decf19ed0bc73ae86141c5924c01f42dbac; anterior às alterações locais |
| URL | Não atribuída |

A EDA e ferramentas de revisão usam `requirements-dev.txt`, separado das dependências do deploy. Os testes e rascunhos College estão em [validacao-college.md](validacao-college.md).

## Antes do envio

Concluir a justificativa individual, reflexão e declaração assinada. Revisar e incluir explicitamente app, src, notebook final, CSV/manifesto tratado, scripts, testes, entregas, prompts, requisitos, configuração e documentação. O arquivo original do autor e o template PDF foram preservados como referências locais.

`data/raw/`, `.venv/`, `tmp/`, `.env` e `.streamlit/secrets.toml` devem permanecer ignorados. Os dois scripts médicos antigos têm guarda para não modificar College.

A [triagem automatizada](auditoria-publicacao.json) procura padrões limitados nos arquivos e blobs históricos; não é certificação de ausência de vazamento. Deve ser complementada pela revisão visual e testes da versão publicada.

## Deploy e aceite

No workspace do Streamlit Community Cloud, criar o app a partir do repositório/main/app.py, escolher a versão Python nas configurações avançadas e acompanhar os logs. Registrar a URL real no README e verificar seu acesso público.

Procedimento conferido nas documentações oficiais de [deploy](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy) e [compartilhamento](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app).

Executar P01–P08 do [checklist](../CHECKLIST.md) em janela anônima, registrando URL/commit/data/executor. O host de navegador estava indisponível para inspeção visual nesta sessão; AppTest e HTTP local não substituem esse aceite.

O tema College já foi confirmado. O que continua dependente do autor é a decisão/justificativa pessoal das métricas, a reflexão, identificação e assinatura. Nenhum conteúdo foi publicado nesta adaptação.
