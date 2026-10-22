import pandas as pd
import plotly.express as px
import streamlit as st

from src.data_loader import load_data

st.set_page_config(
    page_title="Avaliação de Correlação entre Variáveis Quantitativas do Heart Disease Dataset",
    layout="wide",
)

st.title("Avaliação de Correlação entre Variáveis Quantitativas do Heart Disease Dataset")

df = load_data()

# Variáveis quantitativas do estudo (mesma lista VARS_QUANT do notebook de EDA)
VARS_QUANT = ["age", "trestbps", "chol", "thalach", "oldpeak"]

# Sidebar: filtros (variáveis + intervalo)
with st.sidebar:
    st.header("Filtros")

    variaveis = st.multiselect(
        "Variáveis Quantitativas",
        options=VARS_QUANT,
        default=VARS_QUANT,
        help="Selecione as variáveis quantitativas que deseja analisar no dashboard.",
    )

    separar_por_classe = st.toggle(
        "Distinguir por Classe",
        value=False,
        help="Colore a distribuição pela classe (doenca_cardiaca: Normal ou Cardíaco).",
    )

    # Um slider de intervalo para cada variável selecionada
    intervalos = {}
    for var in variaveis:
        if pd.api.types.is_integer_dtype(df[var]):
            minimo, maximo, passo = int(df[var].min()), int(df[var].max()), 1
        else:
            minimo, maximo, passo = float(df[var].min()), float(df[var].max()), 0.1
        intervalos[var] = st.slider(
            f"Intervalo de {var}",
            min_value=minimo,
            max_value=maximo,
            value=(minimo, maximo),
            step=passo,
            key=f"intervalo_{var}",
        )

# Mantém só os pacientes dentro de todos os intervalos escolhidos
df_filtrado = df
for var, (inicio, fim) in intervalos.items():
    df_filtrado = df_filtrado[df_filtrado[var].between(inicio, fim)]

st.caption(f"{len(df_filtrado)} de {len(df)} pacientes dentro dos intervalos escolhidos.")

# Dashboard 1: correlação (heatmap) à esquerda, distribuição (histograma) à direita
col_correlacao, col_distribuicao = st.columns([1, 1.5])

with col_correlacao:
    st.subheader("Correlação")

    if len(variaveis) < 2:
        st.warning("Selecione pelo menos 2 variáveis para calcular a correlação.")
    elif len(df_filtrado) < 2:
        st.warning("Pacientes insuficientes nos intervalos escolhidos para calcular a correlação.")
    else:
        matriz_correlacao = df_filtrado[variaveis].corr()
        fig_correlacao = px.imshow(
            matriz_correlacao,
            text_auto=".2f",
            zmin=-1,
            zmax=1,
            color_continuous_scale="RdBu_r",
            aspect="auto",
        )
        st.plotly_chart(fig_correlacao, width="stretch")

with col_distribuicao:
    st.subheader("Distribuição")

    if not variaveis:
        st.warning("Selecione pelo menos 1 variável para ver a distribuição.")
    elif df_filtrado.empty:
        st.warning("Nenhum paciente dentro dos intervalos escolhidos.")
    else:
        variavel_hist = st.selectbox("Variável do histograma", options=variaveis)
        fig_distribuicao = px.histogram(
            df_filtrado,
            x=variavel_hist,
            color="doenca_cardiaca" if separar_por_classe else None,
            barmode="overlay",
            opacity=0.75,
        )
        st.plotly_chart(fig_distribuicao, width="stretch")

# Dashboard 2: KPIs dos pacientes dentro dos filtros (delta = diferença para o dataset completo)
st.divider()
st.subheader("KPIs")

if df_filtrado.empty:
    st.warning("Nenhum paciente dentro dos intervalos escolhidos para calcular os KPIs.")
else:
    kpi_total, kpi_cardiaco, kpi_idade, kpi_colesterol, kpi_fc = st.columns(5)

    pct_cardiaco = (df_filtrado["doenca_cardiaca"] == "Cardíaco").mean() * 100
    pct_cardiaco_total = (df["doenca_cardiaca"] == "Cardíaco").mean() * 100

    kpi_total.metric(
        "Total de pacientes",
        len(df_filtrado),
        delta=len(df_filtrado) - len(df),
        delta_color="off",
    )
    kpi_cardiaco.metric(
        "% com doença cardíaca",
        f"{pct_cardiaco:.1f}%",
        delta=f"{pct_cardiaco - pct_cardiaco_total:+.1f} p.p.",
        delta_color="inverse",
    )
    kpi_idade.metric(
        "Idade média",
        f"{df_filtrado['age'].mean():.1f} anos",
        delta=f"{df_filtrado['age'].mean() - df['age'].mean():+.1f}",
        delta_color="off",
    )
    kpi_colesterol.metric(
        "Colesterol médio",
        f"{df_filtrado['chol'].mean():.0f} mg/dl",
        delta=f"{df_filtrado['chol'].mean() - df['chol'].mean():+.0f}",
        delta_color="off",
    )
    kpi_fc.metric(
        "FC máx. média",
        f"{df_filtrado['thalach'].mean():.0f} bpm",
        delta=f"{df_filtrado['thalach'].mean() - df['thalach'].mean():+.0f}",
        delta_color="off",
    )
