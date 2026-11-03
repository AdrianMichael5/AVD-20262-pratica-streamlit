# Validação — adaptação para College.csv

**Data:** 2026-11-03. **Executor:** Codex (OpenAI), a pedido de Adrian Michael.
**Versão:** diretório de trabalho, sem commit. Substitui a validação do app Heart Disease.

## Dados e EDA

Download realizado da mesma fonte Kaggle referenciada no notebook original. Base com **777 instituições**, 565 privadas (`Yes`) e 212 não privadas (`No`). As 18 variáveis originais foram mantidas, mais `Expend_log` e `Apps_binned`: **20 colunas**. Nenhuma linha removida.

A EDA foi adaptada a partir do arquivo original, preservado. Foram retirados trechos médicos residuais da cópia final; textos/conclusões assistidos por Gemini foram mantidos com identificação e revisão pessoal pendente. Correlograma limitado às cinco variáveis já comparadas no original para legibilidade; matrizes e distribuições mantêm as 17 variáveis.

**49 células de código executadas, zero erros, 61,109 segundos na execução final.** A exportação reproduziu o CSV do app, conferida por DataFrame com tolerância numérica de `1e-12`, preservando sua representação textual. CSV normalizado em LF; `.gitattributes` mantém CSV/notebook/JSON em LF entre Windows e Linux. Hashes em [execucao-notebook.json](execucao-notebook.json) e [manifesto College](../data/clean/college-manifesto.json).

## Testes

Comando: `python -m unittest discover -s tests -v`.

**10 testes aprovados em 19,390 segundos na execução final**, sem exceções do app nos cenários exercitados:

1. Padrão, toggle por tipo e três métodos de correlação.
2. Tipos No/Yes e seletor das cinco comparações de médias.
3. Seleção das 17 variáveis, de uma e de nenhuma.
4. Alteração/interseção dos cinco sliders padrão e conferência dos KPIs/deltas.
5. Remoção de variável removendo seu filtro.
6. Um registro e amostra vazia.
7. Variável constante e aviso de correlação indefinida.
8. Carregamento do CSV independente do diretório atual.
9. Integridade, categorias, transformações log/tercis, hashes e preservação de Grad.Rate = 118.
10. Média por instituição e grupo ausente sem média zero artificial.

Um primeiro teste falhou na limpeza do temporário no Windows porque o diretório ainda era o diretório atual do processo. O teste foi corrigido para restaurar a pasta antes da limpeza; a suíte completa passou na execução final.

Ambiente: Python 3.12.6, Streamlit 1.66.1, pandas 2.3.3, NumPy 2.5.4, Plotly 6.9.0. Avisos de AppTest/Jupyter não produziram falhas.

## Rascunhos e limites

Dois PNGs College regenerados e conferidos visualmente. Isso não equivale à revisão visual do app: o host de navegador estava indisponível nesta sessão. Os testes são locais, sem deploy ou janela anônima do app publicado.

Os relatórios anteriores de Heart Disease são históricos. Justificativa individual, reflexão, confirmação das ferramentas/skill e PDF assinado continuam pendentes. Escolha do tema College foi confirmada pelo autor.
