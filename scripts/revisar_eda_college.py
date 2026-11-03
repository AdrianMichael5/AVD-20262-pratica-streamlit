# [IA] Codex (OpenAI) - revisão analítica solicitada pelo autor, com atribuição explícita.
"""Corrige resíduos didáticos e confronta conclusões com resultados reproduzíveis."""
from pathlib import Path

import nbformat
import pandas as pd

from conferir_entrega_final import resultados

ROOT = Path(__file__).resolve().parents[1]


def main():
    path = ROOT / "notebooks/eda.ipynb"
    nb = nbformat.read(path, as_version=4)
    df = pd.read_csv(ROOT / "data/clean/dataset.csv")
    r = resultados(df)
    cells = []
    for c in nb.cells:
        s = c.source
        if c.cell_type == "markdown":
            if s.startswith("# EDA — College.csv"):
                c.source = s.replace(
                    "**Limites de autoria:** as conclusões preexistentes assistidas por Gemini precisam de validação/revisão pessoal. O Codex não redigiu novas conclusões ou justificativas em nome do autor.",
                    "**Autoria da revisão:** o autor solicitou ao Codex concluir a revisão da EDA. As respostas e conclusões abaixo foram revisadas com IA a partir de cálculos reproduzíveis; não são apresentadas como produção sem assistência. O arquivo original com os textos Gemini permanece preservado. Esta revisão não certifica o atendimento à exigência de autoria individual do template."
                )
            elif s.startswith("### Renomeando o atributo alvo"):
                c.source = "### Identificação dos grupos\n\n**[IA] Codex - revisão:** `Private` já distingue instituições não privadas (`No`) e privadas (`Yes`). Nenhuma variável alvo foi renomeada."
            elif s.startswith("**Resposta individual:"):
                c.source = "**Resposta revisada com IA:** nenhuma das 18 variáveis originais tem valores ausentes: 0 células faltantes entre 777 instituições. Não foi necessário imputar ou excluir registros por esse motivo. Isso não garante ausência de outros erros de dados."
            elif s.startswith("#### Identificando o mecanismo"):
                c.source = "#### Limites da avaliação de ausência\n\nNão há ausências registradas nesta versão da base. Logo, esta execução não identifica nem testa um mecanismo MCAR, MAR ou MNAR."
            elif s.startswith("**As ausencias ocorrem juntas?"):
                c.source = "**[IA] Codex - revisão:** como não há colunas com ausentes, a lista calculada a seguir fica vazia. Uma análise de coocorrência de ausências não se aplica a esta base."
            elif s.startswith("Com poucos ausentes") or s.startswith("**Nota para quando vocês replicarem") or s.startswith("**Pra discutir:** quantas linhas têm as duas colunas"):
                continue
            elif s.startswith("### Distribuições de dados"):
                c.source = "### Distribuições de dados\n\nA comparação usa `Private`: não privada (`No`, rosa) e privada (`Yes`, roxo). São tipos de instituição; não há classes clínicas neste estudo."
            elif s.startswith("**Como ler:** se os pontos"):
                c.source = f"**[IA] Codex - revisão:** o QQ-plot compara `Expend` com uma distribuição normal. O Shapiro-Wilk dessa coluna resulta em p={r['shapiro_expend']:.3g}; há evidência contra normalidade ao nível de 5%. As {r['shapiro_rejeitados']} quantitativas rejeitam normalidade na amostra conjunta, mas isso não testa normalidade por grupo. O tamanho desta base é 777, não 303; forma, tamanho da amostra e outliers devem ser considerados juntos."
            elif s.startswith("### Métricas de Tendêncial"):
                c.source = "### Medidas de tendência central"
            elif s.startswith("**Pra discutir:** a transformação logarítmica"):
                c.source = f"**Resposta revisada com IA:** a assimetria de `Expend` passa de {r['skewness_expend'][0]:.3f} para {r['skewness_expend'][1]:.3f} em `Expend_log = log1p(Expend)`. A redução não demonstra normalidade. O app mantém `Expend` na escala original e a coluna logarítmica fica como derivada de referência; nenhuma observação foi descartada."
            elif s.startswith("## 5. Estatística Descritiva"):
                c.source = "## 5. Conferência descritiva após as transformações\n\n**[IA] Codex - revisão:** as 777 linhas e os valores originais foram mantidos. Apenas `Expend_log` e, posteriormente, `Apps_binned` são adicionadas. Por isso, as estatísticas das variáveis originais não devem mudar."
            elif s.startswith('### Comparando "antes"'):
                c.source = "### Comparação antes e depois"
            elif s.startswith("**Pra discutir:** os valores mudaram muito?"):
                c.source = "**Resposta revisada com IA:** as estatísticas das colunas originais são iguais antes/depois. Houve 0 linhas removidas, e não remoção de aproximadamente 2%. A comparação a seguir não é uma validação de limpeza de outliers, pois os valores extremos foram preservados."
            elif s.startswith("**O colesterol ainda rejeita normalidade?"):
                c.source = "**Expend após as transformações:** o teste continua na variável original, que não foi alterada. O mesmo p-valor é esperado antes/depois; não é um novo teste de `Expend_log`."
            elif s.startswith('**Pra discutir:** as curvas "antes"'):
                c.source = "**Resposta revisada com IA:** as curvas antes/depois coincidem porque os valores originais de `Apps` e `Expend` são idênticos. Não houve exclusão de linhas ou substituição de valores."
            elif s.startswith("**Pra discutir:** alguma variável qualitativa"):
                c.source = "**Resposta revisada com IA:** `Private` tem 565 instituições privadas (72,7%) e 212 não privadas (27,3%), razão aproximada de 2,67. Os grupos têm tamanhos diferentes; médias por instituição e proporções dentro do grupo evitam confundir contagem de instituições com perfil de cada grupo."
            elif s.startswith("**Pra discutir:** Pearson e Spearman"):
                pair = r["maior_divergencia_correlacao"]
                c.source = f"**Resposta revisada com IA:** a maior diferença absoluta entre Pearson e Spearman entre as quantitativas é em `{' × '.join(pair['par'])}`: Pearson={pair['pearson']:.3f}, Spearman={pair['spearman']:.3f}. Divergência pode refletir forma da relação, valores extremos e empates; sozinha não prova não linearidade. Nenhum coeficiente demonstra causa."
            elif s.startswith("**Pra discutir:** os dois testes concordam"):
                c.source = "**Resposta revisada com IA:** Welch e Mann-Whitney não testam a mesma hipótese. Em `Books`, Welch tem p=0,563 e Mann-Whitney p=0,00181: a divergência não é contradição. Não se escolhe o vencedor pela normalidade da amostra total. A tabela de auditoria final inclui Holm para as 17 comparações de Mann-Whitney. A ANOVA/Kruskal a seguir compara apenas os dois grupos de `Private`; não é um exemplo de três ou mais grupos."
            elif s.lstrip().startswith("from scipy import stats"):
                # Código repetido que estava em uma célula Markdown, sem execução.
                continue
            elif s.startswith("**Pra discutir:** o Qui-Quadrado confirma"):
                c.source = f"**Resposta revisada com IA:** a associação avaliada é `Private × Apps_binned`, não sexo/faixa etária. Qui-quadrado={r['chi2']:.3f}, p={r['p_chi2']:.3g}; menor frequência esperada={r['esperado_minimo']:.2f}; V de Cramér={r['cramer_v']:.3f}. O p-valor avalia independência e V quantifica associação; não se conclui força apenas pelo p-valor nem se certifica fairness institucional por essa tabela."
            elif s.startswith("**Como interpretar:**"):
                c.source = "**Leitura revisada com IA:** Spearman em `Apps × Accept` é 0,979 e em `Apps × Enroll`, 0,926. Já `Apps × Expend` é 0,195: não é uma correlação alta. Rótulos de força são convenções dependentes do contexto; correlação alta entre contagens relacionadas não prova causalidade ou redundância em toda aplicação."
            elif s.startswith("## Revisão individual"):
                c.source = "## Revisão assistida da EDA\n\nO autor solicitou ao Codex concluir esta revisão. As correções e conclusões são explicitamente assistidas por IA; a responsabilidade acadêmica e a compreensão do conteúdo continuam com o autor. O registro pós-assinatura está em `prompts/2026-11-03-revisao-final-eda.md`; o PDF assinado não foi alterado."
            elif "## Principais Conclusões da Análise Exploratória de Dados" in s:
                if not any("AUDITORIA_FINAL_COLLEGE" in cell.source for cell in nb.cells if cell.cell_type == "code"):
                    cells.append(nbformat.v4.new_code_cell('''# [IA] Codex - AUDITORIA_FINAL_COLLEGE: evidências numéricas da revisão.
import json
from conferir_entrega_final import resultados
resumo_revisao = resultados(df)
display(pd.DataFrame(resumo_revisao["medias_por_tipo"]).T)
display(pd.DataFrame(resumo_revisao["testes"]).set_index("variavel"))
print("Ausentes:", resumo_revisao["ausentes"], "| Duplicadas:", resumo_revisao["duplicadas"])
print("Spearman Apps:", resumo_revisao["spearman_apps"])
print("Qui-quadrado:", resumo_revisao["chi2"], "p:", resumo_revisao["p_chi2"], "V de Cramér:", resumo_revisao["cramer_v"])
(RAIZ / "entregas/revisao-eda-resultados.json").write_text(json.dumps(resumo_revisao, ensure_ascii=False, indent=2, default=int) + "\\n", encoding="utf-8", newline="\\n")
'''))
                c.source = f'''## Principais Conclusões da Análise Exploratória de Dados

**Revisão com assistência do Codex, a pedido do autor em 03/11/2026.** Substitui as conclusões Gemini inconsistentes da cópia anterior; o original permanece preservado. Evidências na célula acima e em `entregas/revisao-eda-resultados.json`.

1. **Integridade não é ausência de anomalias:** há 777 instituições, 0 valores ausentes e 0 linhas duplicadas nas 18 variáveis originais. Entretanto, existe 1 registro de `Grad.Rate = 118`, fora da escala percentual esperada. Ele foi preservado para reprodução, não certificado como válido.
2. **Distribuição e transformação:** as 17 quantitativas rejeitam normalidade conjunta pelo Shapiro-Wilk a 5%. `Expend` tem assimetria {r['skewness_expend'][0]:.3f}, reduzida a {r['skewness_expend'][1]:.3f} com `log1p`. Isso não garante normalidade nem substitui análise por grupo.
3. **Comparações observadas, sem causalidade:** nesta amostra, a média de Apps é 5.729,920 em No e 1.977,929 em Yes; Expend é 7.458,316 e 10.486,354, respectivamente. As 17 comparações de distribuições por Mann-Whitney permanecem com p ajustado por Holm abaixo de 0,05. Isso não demonstra que o tipo de instituição cause os resultados nem que o efeito seja grande em todas as variáveis; o caso Books ilustra que Welch e Mann-Whitney respondem a hipóteses diferentes.
4. **Associações precisam ser descritas corretamente:** Spearman Apps–Accept={r['spearman_apps']['Accept']:.3f} e Apps–Enroll={r['spearman_apps']['Enroll']:.3f}; Apps–Expend={r['spearman_apps']['Expend']:.3f}, portanto não sustenta a alegação antiga de correlação alta entre candidaturas e gasto por aluno. Em Private × tercis de Apps, p={r['p_chi2']:.3g} e V de Cramér={r['cramer_v']:.3f}; 68,87% de No estão no tercil alto, contra 20,00% de Yes.
5. **Escopo e limites:** nenhuma linha/valor original foi removido; as diferenças antes/depois das variáveis originais são nulas por construção. A base é histórica e observacional, com grupos desiguais; médias simples não são ponderadas por alunos. Não se generalizam resultados a instituições atuais nem se deduz causalidade ou justiça algorítmica.
'''
            elif "## Justificativa das Decisões de EDA e Escolhas" in s:
                c.source = '''## Justificativa das Decisões de EDA e Escolhas

**[IA] Codex - revisão técnica solicitada pelo autor.** Não é texto apresentado como autoria individual sem assistência.

- **Esquema:** Private já define No/Yes; mantidas as 18 variáveis originais, sem alvo clínico e sem renomeação de classe médica.
- **Ausentes/duplicadas:** contagens iguais a zero; sem imputação e sem exclusão. Não se afirma mecanismo MCAR/MAR/MNAR.
- **Extremos:** mantidos para preservar a base usada no notebook. Raridade estatística não prova legitimidade; Grad.Rate=118 é anomalia que exige conferência da fonte. Não houve winsorização ou truncamento silencioso.
- **Derivadas:** Expend_log usa log1p; Apps_binned usa tercis de Apps na base completa. Não se recalculam tercis por recorte no app.
- **Comparações:** mantidos Welch e Mann-Whitney como métodos com hipóteses distintas. Acrescentado ajuste de Holm às 17 comparações Mann-Whitney, para explicitar a família de testes. Significância não é tamanho de efeito nem causalidade.
- **Categorias:** Qui-quadrado cruza Private com Apps_binned; V de Cramér complementa o p-valor. Isso não é avaliação de fairness de sexo/faixa etária.
- **Reprodução e apresentação:** 17 variáveis nas matrizes/distribuições; correlograma ilustrativo limitado às cinco comparações já usadas na EDA. A exportação mantém as 18 originais e duas derivadas.

Fontes metodológicas: [Mann-Whitney (SciPy)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html), [V de Cramér (SciPy)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.contingency.association.html) e [ajustes de múltiplos testes/Holm (statsmodels)](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html). O ajuste foi implementado com NumPy, sem nova dependência.
'''
        cells.append(c)
    nb.cells = cells
    path.write_bytes(nbformat.writes(nb).replace("\r\n", "\n").encode("utf-8"))
    print("Revisão assistida aplicada; executar a EDA para renovar saídas e registro de hashes.")


if __name__ == "__main__":
    main()
