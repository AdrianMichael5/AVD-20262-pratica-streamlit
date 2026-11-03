# Preparação da publicação — College.csv

**Data:** 2026-11-03. **Executor:** Codex (OpenAI), solicitado por Adrian Michael.
**Estado:** código e entregáveis enviados a main; URL de publicação fornecida pelo autor e registrada no README. Aceite publicado pendente.

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
| Versão da entrega enviada | b1bb1db9d8e9c746880180589ee0e36f8f7eb951; código College e entregáveis |
| URL informada pelo autor | https://college-adrian-avd.streamlit.app/ |

A EDA e ferramentas de revisão usam `requirements-dev.txt`, separado das dependências do deploy. Os testes e rascunhos College estão em [validacao-college.md](validacao-college.md).

## Antes da entrega acadêmica final

Concluir a justificativa individual, reflexão e declaração assinada. Revisar e incluir explicitamente app, src, notebook final, CSV/manifesto tratado, scripts, testes, entregas, prompts, requisitos, configuração e documentação. O arquivo original do autor e o template PDF foram preservados como referências locais.

`data/raw/`, `.venv/`, `tmp/`, `.env` e `.streamlit/secrets.toml` devem permanecer ignorados. Os dois scripts médicos antigos têm guarda para não modificar College.

A [triagem automatizada](auditoria-publicacao.json) procura padrões limitados nos arquivos e blobs históricos; não é certificação de ausência de vazamento. Deve ser complementada pela revisão visual e testes da versão publicada.

## Deploy e aceite

No workspace do Streamlit Community Cloud, criar o app a partir do repositório/main/app.py, escolher a versão Python nas configurações avançadas e acompanhar os logs. Registrar a URL real no README e verificar seu acesso público.

Procedimento conferido nas documentações oficiais de [deploy](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy) e [compartilhamento](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app).

Executar P01–P08 do [checklist](../CHECKLIST.md) em janela anônima, registrando URL/commit/data/executor. O host de navegador estava indisponível para inspeção visual nesta sessão; AppTest e HTTP local não substituem esse aceite.

O tema College e a identificação já foram fornecidos. O autor delegou a adoção da proposta técnica de público/métricas; justificativa pessoal, reflexão e assinatura continuam pendentes. O autor forneceu o endereço de publicação após a orientação de deploy. A versão instalada do CLI Streamlit não possui comando de deploy; o host de navegador desta sessão continua indisponível para o aceite visual.

### Verificação do endereço em 03/11/2026

Solicitações HTTP sem autenticação à raiz e a `/_stcore/health` responderam 200, com conteúdo HTML. O segundo endereço não retornou o texto `ok`; portanto, não se certifica saúde do runtime por esse resultado. Os testes de abas/widgets e de acesso em janela anônima permanecem pendentes. Nenhum desses testes foi marcado como aprovado apenas pela resposta HTTP.
