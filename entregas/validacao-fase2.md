# Histórico — validação Heart Disease (supersedida)

**Atenção:** este relatório registra a versão médica anterior. A versão atual é College; sua evidência está em [validacao-college.md](validacao-college.md). Links de nomes genéricos para notebook/CSV podem apontar para os artefatos atuais.

**Data:** 2026-11-03, America/Fortaleza.
**Executor:** Codex (OpenAI), a pedido de Adrian Michael.
**Código validado:** diretório de trabalho após a implementação da fase 2, ainda sem commit. Base histórica local: `1c8f1de`.

## Resultado

**Oito testes aprovados em 6,120 segundos**, sem exceções do app nos cenários exercitados. Comando executado na raiz:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Ambiente: Windows, Python 3.12.6, Streamlit 1.66.1, pandas 2.3.3, Plotly 6.9.0. Dependências instaladas em `.venv/` a partir de `requirements.txt`; o ambiente não é versionado. O AppTest emitiu o aviso `missing ScriptRunContext` do contexto de teste, sem falha na suíte.

## Cenários cobertos

| Teste em `tests/test_app.py` | Evidência conferida |
| --- | --- |
| `test_padrao_e_toggle` | Duas abas; cinco histogramas; cinco valores de KPIs calculados contra o CSV; três gráficos do perfil; toggle gera duas séries por histograma. |
| `test_selecao_e_remocao_de_filtro` | Intervalo de idade 45–55; seleção de uma variável e nenhuma; filtro removido junto à variável; avisos e perfil coerentes. |
| `test_cada_slider_e_intersecao` | Alteração dos cinco sliders em sequência; recorte pela interseção e atualização dos cinco KPIs a cada interação. |
| `test_variavel_constante_e_amostra_vazia` | Idade fixada em 45 produz aviso de correlação indefinida; combinação sem registros não exibe métricas/gráficos enganosos nem lança exceção. |
| `test_um_participante_e_uma_classe` | Recorte com um participante; correlação indisponível; demais gráficos e KPIs renderizados; restauração do intervalo recupera a base completa. |
| `test_denominadores_e_grupos_ausentes` | Dados controlados produzem 50% e 100% nos respectivos grupos; grupos vazios ficam indefinidos; classe ausente aparece com contagem zero. |
| `test_migracao_preserva_todas_as_outras_colunas` | Comparação com o CSV do HEAD local comprova mesma quantidade/ordem de linhas e igualdade textual de todas as colunas exceto a última, `faixa_etaria`. |
| `test_rotulos_e_fronteiras_da_eda` | Expressão real de `pd.cut` do notebook testada em 44, 45, 46, 54, 55, 56, 64, 65 e 66; todas as linhas do CSV conferidas contra os limites corrigidos. |

## Correção dos dados

O script `scripts/corrigir_faixas_etarias.py` foi executado uma vez. Ele preserva a divisão original `(0,45]`, `(45,55]`, `(55,65]`, `(65,100]` e ajusta seus rótulos para **Até 45**, **46–55**, **56–65** e **Acima de 65**. A base continua com 297 registros, sendo 160 `Normal` e 137 `Cardíaco`.

A célula correspondente da EDA foi corrigida. As saídas de código a partir dessa célula foram limpas, inclusive gráficos que continham rótulos antigos; nenhuma reexecução integral da EDA é alegada. Reexecutar o notebook e conferir a exportação na fase 3.

## Limites e próximo aceite

AppTest executa o código e as interações de widgets sem navegador. Esta validação não comprova aparência visual, clique nas abas em navegador, acesso público, ausência de vazamento no histórico ou funcionamento em janela anônima. Os testes P01–P08 de `CHECKLIST.md` continuam pendentes até a publicação.
