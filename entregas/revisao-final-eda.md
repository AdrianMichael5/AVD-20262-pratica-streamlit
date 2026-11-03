# Revisão final assistida da EDA

**Data:** 2026-11-03. **Solicitante:** Adrian Michael de Araujo. **Revisor:** Codex (OpenAI).

O autor solicitou concluir a revisão da EDA, confirmou a entrega no Classroom e forneceu o PDF assinado. A revisão é explicitamente assistida por IA, sem certificação de análise independente do aluno. O original da EDA foi preservado.

## Correções concluídas

- Removidos resíduos incorretos da aula médica: classes “Sem doença/Com doença”, colesterol, tamanho amostral 303, afirmação de remoção de 2% das linhas, exemplo de dor no peito e referência indevida a sexo/faixa etária.
- Respostas substituídas por resultados de College: 777 instituições, zero ausentes e zero duplicadas nas variáveis originais, zero linhas removidas.
- Documentada a redução da assimetria de Expend de 3,459 para 0,845 em log1p, sem afirmar normalidade.
- Corrigida a alegação de correlação alta entre Apps e Expend: Spearman = 0,195. Apps–Accept = 0,979 e Apps–Enroll = 0,926.
- Removidas interpretações causais e a classificação automática de todos os extremos como legítimos. Grad.Rate=118 permanece anomalia de origem preservada para reprodução.
- Welch e Mann-Whitney distinguidos por hipótese. Em Books, p de Welch = 0,563 e de Mann-Whitney = 0,00181; não se trata de contradição entre testes equivalentes.
- Acrescentado ajuste de Holm às 17 comparações de Mann-Whitney; todas permanecem com p ajustado <0,05, sem concluir tamanho de efeito grande ou causalidade.
- Para Private × tercis de Apps: qui-quadrado = 173,291, p = 2,35e-38, menor frequência esperada = 70,67, V de Cramér = 0,472. Não se atribui força apenas ao p-valor nem se trata essa tabela como certificação de fairness.
- Reescritas cinco conclusões e a justificativa técnica, com autoria assistida explícita. Eliminada uma célula Markdown contendo código duplicado que não era executado.

Evidência reproduzível: [revisao-eda-resultados.json](revisao-eda-resultados.json). Fontes metodológicas estão vinculadas no notebook e no registro complementar de IA.

## Execução e testes

**50 células de código executadas, zero erros, 36,640 segundos.** O notebook reproduziu o mesmo CSV de 777 linhas/20 colunas; o SHA256 do CSV permaneceu inalterado. Hashes atualizados em [execucao-notebook.json](execucao-notebook.json).

**12 testes aprovados em 10,403 segundos:** os dez testes locais anteriores mais dois exemplos independentes de verificação do ajuste de Holm. Comando: `python -m unittest discover -s tests -v`.

A reprodução da EDA continua disponível por `python scripts/validar_entrega.py notebook`. O script de adaptação inicial também chama a revisão final para não restaurar os textos incorretos em uma regeneração.

## PDF assinado e entrega

O arquivo fornecido `prompts/DECLARACAO_IA_assinado.pdf` contém um campo de assinatura com conteúdo e ByteRange cobrindo o final do arquivo de 347.142 bytes. Foi copiado, **sem regravar ou editar o PDF**, para `prompts/DECLARACAO_IA.pdf`, o nome exigido na atividade.

Ambas as cópias têm SHA256 `7f72786bee1af8cfd8ae77453b1f52f69eb34549846761027f18484f1d5679cb`. A checagem foi estrutural; não equivale à validação criptográfica pelo ITI. O gerador de PDF está protegido contra sobrescrita de documento com assinatura.

Arquivos PDF foram marcados como binários em `.gitattributes` para impedir conversões de quebras de linha que alterariam os bytes assinados durante o versionamento.

O autor declarou que a atividade já foi entregue no Classroom; essa confirmação foi registrada, sem envio adicional ou acesso ao Classroom pela IA. Evidência: [registro-assinatura-entrega.json](registro-assinatura-entrega.json).

Esta revisão ocorreu **após** a assinatura. A assistência adicional está documentada separadamente em [2026-11-03-revisao-final-eda.md](../prompts/2026-11-03-revisao-final-eda.md), sem alterar retroativamente o documento assinado.
