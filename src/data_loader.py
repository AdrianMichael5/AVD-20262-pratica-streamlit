# [IA] Codex (OpenAI) - carregamento de College com caminho independente do diretório atual.
from pathlib import Path

import pandas as pd
import streamlit as st

DATASET = Path(__file__).resolve().parents[1] / "data/clean/dataset.csv"


@st.cache_data
def load_data(path=None):
    """O app usa apenas o CSV tratado local; sem Kaggle/autenticação em execução."""
    return pd.read_csv(DATASET if path is None else path)
