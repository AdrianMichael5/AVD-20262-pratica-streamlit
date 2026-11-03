# [IA] Codex (OpenAI) - configuração e cálculos de College, seguindo variáveis da EDA.
"""Dicionário e agregações descritivas de College.csv."""

VARS_QUANT = ["Apps", "Accept", "Enroll", "Top10perc", "Top25perc", "F.Undergrad",
              "P.Undergrad", "Outstate", "Room.Board", "Books", "Personal", "PhD",
              "Terminal", "S.F.Ratio", "perc.alumni", "Expend", "Grad.Rate"]
# As cinco variáveis já comparadas por média no notebook original.
INDICADORES = ["Apps", "Accept", "Enroll", "Expend", "Grad.Rate"]
TIPOS = ["No", "Yes"]
TIPO_LABEL = {"No": "Não privada", "Yes": "Privada"}
CORES = {"No": "#2563eb", "Yes": "#7c3aed"}
ROTULOS = {
    "Apps": "Candidaturas recebidas", "Accept": "Candidaturas aceitas",
    "Enroll": "Novos matriculados", "Top10perc": "Ingressantes no top 10% do ensino médio (%)",
    "Top25perc": "Ingressantes no top 25% do ensino médio (%)",
    "F.Undergrad": "Graduandos em tempo integral", "P.Undergrad": "Graduandos em tempo parcial",
    "Outstate": "Anuidade para alunos de outro estado", "Room.Board": "Moradia e alimentação",
    "Books": "Custo estimado de livros", "Personal": "Despesas pessoais estimadas",
    "PhD": "Docentes com doutorado (%)", "Terminal": "Docentes com grau terminal (%)",
    "S.F.Ratio": "Relação estudantes/docentes", "perc.alumni": "Ex-alunos doadores (%)",
    "Expend": "Gasto educacional por aluno", "Grad.Rate": "Taxa de graduação (%)",
    "Private": "Tipo de instituição",
}
METRICAS = {
    "Apps": "Candidaturas médias", "Accept": "Aceitações médias",
    "Enroll": "Novos matriculados médios", "Expend": "Gasto médio por aluno",
    "Grad.Rate": "Graduação média",
}


def medias_por_tipo(df, variavel):
    """Tipo ausente tem média indefinida; nunca ganha zero artificial."""
    resumo = df.groupby("Private")[variavel].agg(["mean", "size"]).reindex(TIPOS)
    resumo.columns = ["Média", "Instituições"]
    resumo["Instituições"] = resumo["Instituições"].fillna(0).astype(int)
    return resumo.rename_axis("Private").reset_index()


def formatar_indicador(variavel, valor):
    if variavel == "Grad.Rate":
        return f"{valor:.1f}%"
    return f"{valor:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")
