import streamlit as st

from src.data_loader import load_data

st.set_page_config(
    page_title="Meu Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("Meu Dashboard")

# df = load_data()

# TODO: sidebar (título, instruções, navegação)

# TODO: filtros (st.sidebar.selectbox / multiselect / slider)

# TODO: Dashboard 1 — correlação + distribuição (Aula 21)

# TODO: Dashboard 2 — KPIs (Aula 22)
