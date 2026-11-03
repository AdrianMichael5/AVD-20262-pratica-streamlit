# Público e justificativa técnica — College.csv

**Responsável:** Adrian Michael de Araujo, turma 5A. **Data:** 03/11/2026.

**Autoria desta proposta:** Codex (OpenAI), após o pedido do autor “Faça oque fizer mais sentido”. É uma proposta técnica assistida, não uma justificativa individual escrita pelo aluno. O template exige revisão e justificativa pessoal; sua origem permanece declarada.

## Público e objetivo adotados na implementação

**Público:** coordenação de planejamento institucional de ensino superior.

**Objetivo:** comparar perfis de demanda, ingresso e recursos entre instituições privadas e não privadas da base College, usando os mesmos indicadores já comparados na EDA. O painel é descritivo; não avalia candidaturas individuais nem representa a situação atual das instituições.

## Cinco indicadores

| Indicador | Cálculo | Relevância técnica para o objetivo | Limitação |
| --- | --- | --- | --- |
| Candidaturas médias | Média simples de Apps | Resume o volume de procura registrado por instituição. | Não conta pessoas únicas nem mede qualidade ou chance individual de ingresso. |
| Aceitações médias | Média simples de Accept | Permite comparar o volume de candidaturas aceitas com o perfil de demanda. | É contagem média, não taxa de aceitação; instituições de portes diferentes não são equivalentes. |
| Novos matriculados médios | Média simples de Enroll | Resume o ingresso efetivamente registrado nas instituições do recorte. | Não é o total de graduandos e não demonstra causalidade com Apps/Accept. |
| Gasto médio por aluno | Média simples de Expend | Acrescenta a dimensão de recursos educacionais por aluno à comparação institucional. | Valores históricos da fonte; não são custos atuais e a média não é ponderada pelo porte. |
| Graduação média | Média simples de Grad.Rate | Acrescenta uma dimensão de conclusão ao perfil de entrada e recursos. | Não é taxa agregada dos alunos; a fonte contém valor 118, preservado e sinalizado para revisão. |

Essas cinco variáveis já constavam do bloco `variables_to_compare` do notebook fornecido. Os deltas comparam a média do recorte à base completa; em Grad.Rate a unidade é ponto percentual. Nenhum delta representa evolução no tempo.

## Três visuais

- **Médias por tipo:** comparação entre No/Yes com seletor do indicador. Um tipo sem registros é omitido, sem média zero artificial.
- **Dispersão Apps × Accept:** mostra os pares de contagens de cada instituição, com cor por tipo, sem extrapolar para causalidade ou decisão individual.
- **Boxplot de Expend por tipo:** complementa a média com mediana e quartis; os extremos continuam nos cálculos, embora seus pontos isolados fiquem ocultos no resumo visual.

Todos reaproveitam formas de comparação presentes na EDA. Os filtros são compartilhados; médias e gráficos usam exatamente as mesmas linhas.

## Verificação e revisão individual

Dez testes automatizados locais foram executados pelo Codex; a EDA reproduziu o CSV do app. Isso não equivale à confirmação de compreensão ou verificação pessoal do aluno.

- [x] Implementação alinhada ao público técnico e aos blocos da EDA, conforme delegação do autor.
- [ ] Autor revisou a proposta e escreveu sua própria justificativa, conforme o template.
- [ ] Autor conferiu pessoalmente os cálculos e consegue explicar suas limitações.
- [ ] Autor registrou na reflexão o que manteve, modificou ou rejeitou da assistência.
