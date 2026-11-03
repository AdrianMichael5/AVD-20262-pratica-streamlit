# Planejamento — College.csv

**Data:** 2026-11-03. **Tema:** confirmado por Adrian Michael (“use college.csv”).
**Preparação técnica:** Codex (OpenAI). Público, escolhas e justificativa individuais: pendentes.

Os rascunhos são uma revisão do planejamento após o app inicial. Não comprovam planejamento anterior ao código e usam formas ilustrativas, sem dados calculados.

## Base da adaptação

O notebook fornecido pelo autor já contém 17 variáveis quantitativas, comparação por `Private`, médias de `Apps`, `Accept`, `Enroll`, `Expend` e `Grad.Rate`, dispersão Apps × Accept e boxplots por tipo. A implementação reaproveita esses blocos; não apresenta suas escolhas como decisão individual concluída.

**Público de trabalho exibido:** planejamento institucional. O autor deve confirmar seu público e justificar os indicadores em [justificativa-metricas.md](justificativa-metricas.md). As propostas anteriores sobre cardiologia foram supersedidas.

## Dashboard 1 — laboratório

- Seleção das 17 variáveis quantitativas originais; as cinco do bloco de médias são o padrão.
- Métodos Spearman (padrão), Pearson e Kendall; escala do mapa entre -1 e 1, coeficientes nas células.
- Um histograma por variável selecionada, em grade de duas colunas.
- Cores por tipo de instituição quando o toggle está ativo.
- Avisos para nenhuma variável, amostra vazia, menos de dois registros e correlação indefinida por constante.

## Dashboard 2 — comparação institucional

| Elemento | Cálculo/variáveis | Origem técnica |
| --- | --- | --- |
| KPI 1 | Média de Apps | Bloco `variables_to_compare` do notebook |
| KPI 2 | Média de Accept | Mesmo bloco |
| KPI 3 | Média de Enroll | Mesmo bloco |
| KPI 4 | Média de Expend | Mesmo bloco |
| KPI 5 | Média de Grad.Rate, em % | Mesmo bloco |
| Visual 1 | Média por Private, com seletor entre as cinco variáveis | Comparação por médias já presente na EDA |
| Visual 2 | Dispersão Apps × Accept, cor por Private | Dispersão já presente na EDA |
| Visual 3 | Boxplot de Expend por Private | Comparação de distribuições da EDA |

Médias simples por instituição, sem ponderação por alunos. Deltas = média filtrada menos média da base completa; para Grad.Rate, diferença em pontos percentuais. Tipo ausente não recebe média zero. Não se recalculam os tercis de Apps quando o usuário filtra.

A base é histórica; os valores de gasto não são custos atuais. Valores originais de Grad.Rate acima de 100 não são corrigidos automaticamente; são sinalizados. Escolha e interpretação permanecem responsabilidade do autor.

## Filtros e navegação

Duas abas: **Laboratório** e **Comparação institucional**. Sidebar compartilhada: seleção de variáveis, tipo Todos/No/Yes, toggle de cores e slider por variável selecionada. Os intervalos são inclusivos e aplicados por interseção.

Retirar uma variável remove seu filtro. A seleção altera os gráficos do laboratório; os cinco KPIs e três visuais do segundo painel mantêm suas definições e usam os mesmos registros filtrados. Sem variáveis selecionadas, o filtro de tipo continua ativo. Sem instituições, exibir avisos e omitir métricas/gráficos.

## Rascunhos

- [Dashboard 1](rascunho_dashboard1.png)
- [Dashboard 2](rascunho_dashboard2.png)

Gerados por [gerar-rascunhos.ps1](gerar-rascunhos.ps1), autoria assistida e data nas imagens; conferidos visualmente. Proporções podem se ajustar na implementação Streamlit. Reprodução no Windows:

```powershell
powershell -NoProfile -File entregas/gerar-rascunhos.ps1
```
