# [IA] Codex (OpenAI) - adaptação para College.csv a pedido do autor.
import pandas as pd
import plotly.express as px
import streamlit as st

from src.analysis import (
    CORES, INDICADORES, METRICAS, ROTULOS, TIPO_LABEL, TIPOS, VARS_QUANT,
    formatar_indicador, medias_por_tipo,
)
from src.data_loader import load_data

st.set_page_config(page_title="College | Análise institucional", layout="wide")
st.title("College — análise de instituições de ensino")
st.caption("Dados históricos de instituições dos EUA. Explore distribuições e comparações por tipo.")
df = load_data()

with st.sidebar:
    st.header("Filtros das instituições")
    variaveis = st.multiselect(
        "Variáveis quantitativas", options=VARS_QUANT, default=INDICADORES, key="variaveis",
        format_func=lambda var: f"{ROTULOS[var]} ({var})",
        help="Seleciona as variáveis da correlação e dos histogramas.",
    )
    tipo = st.selectbox(
        "Tipo de instituição", options=["Todos", *TIPOS], key="tipo",
        format_func=lambda value: TIPO_LABEL.get(value, value),
    )
    separar = st.toggle("Distinguir por tipo", key="separar", help="Separa as cores dos histogramas por Private.")
    st.caption(
        "Os filtros afetam as duas abas. Retirar uma variável remove seu filtro de intervalo. "
        "Sem variáveis selecionadas, permanece apenas o filtro de tipo."
    )
    intervalos = {}
    for var in variaveis:
        inteiro = pd.api.types.is_integer_dtype(df[var])
        minimo = int(df[var].min()) if inteiro else float(df[var].min())
        maximo = int(df[var].max()) if inteiro else float(df[var].max())
        intervalos[var] = st.slider(
            f"{ROTULOS[var]} ({var})", min_value=minimo, max_value=maximo,
            value=(minimo, maximo), step=1 if inteiro else 0.1, key=f"intervalo_{var}",
        )

recorte = df if tipo == "Todos" else df[df.Private.eq(tipo)]
for var, (inicio, fim) in intervalos.items():
    recorte = recorte[recorte[var].between(inicio, fim)]
st.caption(f"{len(recorte)} de {len(df)} instituições nos filtros selecionados.")
lab, painel = st.tabs(["Laboratório", "Comparação institucional"])

with lab:
    st.header("Distribuição e correlação")
    metodo = st.selectbox("Método de correlação", ["spearman", "pearson", "kendall"], key="metodo", format_func=str.title)
    st.caption("Coeficientes descritivos: associação não demonstra causalidade.")
    if len(variaveis) < 2:
        st.warning("Selecione pelo menos 2 variáveis para calcular a correlação.")
    elif len(recorte) < 2:
        st.warning("Instituições insuficientes para calcular a correlação.")
    else:
        matriz = recorte[variaveis].corr(method=metodo)
        if matriz.isna().any().any():
            st.info("Variáveis constantes têm correlação indefinida, exibida sem valor no mapa.")
        fig = px.imshow(
            matriz, text_auto=".2f", zmin=-1, zmax=1,
            color_continuous_scale="RdBu_r", aspect="auto", labels={"color": metodo.title()},
        )
        st.plotly_chart(fig, width="stretch", key="correlacao")
    st.subheader("Distribuições")
    if not variaveis:
        st.warning("Selecione pelo menos 1 variável para ver as distribuições.")
    elif recorte.empty:
        st.warning("Nenhuma instituição nos filtros selecionados.")
    else:
        for inicio in range(0, len(variaveis), 2):
            for coluna, var in zip(st.columns(2), variaveis[inicio:inicio + 2]):
                with coluna:
                    fig = px.histogram(
                        recorte, x=var, color="Private" if separar else None,
                        category_orders={"Private": TIPOS}, color_discrete_map=CORES,
                        color_discrete_sequence=[CORES["No"]], barmode="overlay",
                        opacity=0.75, labels=ROTULOS, title=f"{ROTULOS[var]} ({var})",
                    )
                    fig.update_layout(yaxis_title="Instituições")
                    st.plotly_chart(fig, width="stretch", key=f"hist_{var}")

with painel:
    st.header("Comparação institucional")
    st.write("Público de trabalho: planejamento institucional. Comparações descritivas de demanda, ingresso e recursos.")
    st.caption(
        "Médias simples entre instituições, sem ponderação por número de alunos. "
        "Os valores da fonte são históricos e não representam custos atuais."
    )
    if recorte.empty:
        st.warning("Nenhuma instituição nos filtros para calcular os indicadores.")
    else:
        st.caption("Deltas: recorte menos a base completa, sem comparação temporal ou meta.")
        for coluna, var in zip(st.columns(5), INDICADORES):
            media = recorte[var].mean()
            unidade = " p.p." if var == "Grad.Rate" else ""
            coluna.metric(
                METRICAS[var], formatar_indicador(var, media),
                delta=f"{media - df[var].mean():+.1f}{unidade}", delta_color="off",
            )
        esquerda, direita = st.columns(2)
        with esquerda:
            comparar = st.selectbox(
                "Variável para comparar médias", INDICADORES, key="comparar", format_func=lambda var: ROTULOS[var],
            )
            resumo = medias_por_tipo(recorte, comparar)
            dados = resumo[resumo["Instituições"] > 0]
            fig = px.bar(
                dados, x="Private", y="Média", color="Private", text="Média",
                color_discrete_map=CORES, category_orders={"Private": TIPOS},
                custom_data=["Instituições"], title=f"Média de {comparar} por tipo",
                labels={"Private": "Tipo", "Média": ROTULOS[comparar]},
            )
            fig.update_traces(texttemplate="%{y:.1f}", hovertemplate="%{x}<br>Média: %{y:.2f}<br>Instituições: %{customdata[0]}<extra></extra>")
            fig.update_layout(showlegend=False)
            fig.update_xaxes(tickvals=TIPOS, ticktext=[TIPO_LABEL[t] for t in TIPOS])
            st.plotly_chart(fig, width="stretch", key="medias_tipo")
            ausentes = resumo.loc[resumo["Instituições"].eq(0), "Private"].tolist()
            if ausentes:
                st.caption("Tipos sem instituições no recorte, omitidos: " + ", ".join(TIPO_LABEL[t] for t in ausentes))
        with direita:
            fig = px.scatter(
                recorte, x="Apps", y="Accept", color="Private", labels=ROTULOS,
                color_discrete_map=CORES, category_orders={"Private": TIPOS},
                title="Candidaturas recebidas e aceitas",
            )
            st.plotly_chart(fig, width="stretch", key="candidaturas")
        fig = px.box(
            recorte, x="Private", y="Expend", color="Private", points=False,
            color_discrete_map=CORES, category_orders={"Private": TIPOS},
            labels=ROTULOS, title="Distribuição do gasto educacional por aluno",
        )
        fig.update_layout(showlegend=False)
        fig.update_xaxes(tickvals=TIPOS, ticktext=[TIPO_LABEL[t] for t in TIPOS])
        st.plotly_chart(fig, width="stretch", key="gastos_tipo")
        st.caption("Caixas mostram quartis e mediana; pontos extremos isolados estão ocultos no gráfico, mas entram nas médias.")
        if recorte["Grad.Rate"].gt(100).any():
            st.info("A fonte contém Grad.Rate acima de 100%. O valor original foi preservado; confira essa anomalia ao usar o indicador.")
