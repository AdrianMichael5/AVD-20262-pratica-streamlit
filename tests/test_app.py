# [IA] Codex (OpenAI) - testes College: filtros, agregações e integridade.
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd
from streamlit.testing.v1 import AppTest

from src.analysis import INDICADORES, TIPOS, VARS_QUANT, formatar_indicador, medias_por_tipo
from src.data_loader import load_data

ROOT = Path(__file__).resolve().parents[1]
DF = pd.read_csv(ROOT / "data/clean/dataset.csv")


class DadosTest(unittest.TestCase):
    def test_integridade_e_transformacoes_da_eda(self):
        self.assertEqual(DF.shape, (777, 20))
        self.assertFalse(DF.isna().any().any())
        self.assertEqual(DF.Private.value_counts().to_dict(), {"Yes": 565, "No": 212})
        self.assertEqual(DF.Apps.sum(), 2332273)
        self.assertEqual(DF.Apps.iloc[:3].tolist(), [1660, 2186, 1428])
        np.testing.assert_allclose(DF.Expend_log, np.log1p(DF.Expend))
        esperado = pd.qcut(DF.Apps, 3, labels=["Baixo", "Médio", "Alto"]).astype(str)
        self.assertEqual(DF.Apps_binned.tolist(), esperado.tolist())
        # A anomalia original não é eliminada ou truncada silenciosamente.
        self.assertEqual(DF["Grad.Rate"].max(), 118)
        manifesto = json.loads((ROOT / "data/clean/college-manifesto.json").read_text(encoding="utf-8"))
        self.assertEqual(manifesto["clean_sha256"], hashlib.sha256((ROOT / "data/clean/dataset.csv").read_bytes()).hexdigest())

    def test_media_por_instituicao_e_tipo_ausente(self):
        dados = pd.DataFrame({"Private": ["No", "No", "Yes"], "Apps": [100, 300, 1000]})
        resumo = medias_por_tipo(dados, "Apps")
        self.assertEqual(resumo["Média"].tolist(), [200, 1000])
        self.assertEqual(resumo["Instituições"].tolist(), [2, 1])
        resumo = medias_por_tipo(dados.iloc[:2], "Apps")
        self.assertTrue(pd.isna(resumo["Média"].iloc[1]))
        self.assertEqual(resumo["Instituições"].tolist(), [2, 0])

    def test_carregamento_independe_da_pasta_atual(self):
        anterior = Path.cwd()
        (ROOT / "tmp").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / "tmp") as pasta:
            try:
                os.chdir(pasta)
                load_data.clear()
                pd.testing.assert_frame_equal(load_data(), DF)
            finally:
                os.chdir(anterior)


class AppTestCase(unittest.TestCase):
    def app(self):
        app = AppTest.from_file(str(ROOT / "app.py"), default_timeout=45).run()
        self.assertFalse(app.exception)
        return app

    def conferir(self, app, esperado, n_hist):
        self.assertFalse(app.exception)
        self.assertEqual([t.label for t in app.tabs], ["Laboratório", "Comparação institucional"])
        specs = [json.loads(c.proto.spec) for c in app.get("plotly_chart")]
        hist = [s for s in specs if s["data"][0]["type"] == "histogram"]
        self.assertEqual(len(hist), n_hist if len(esperado) else 0)
        if esperado.empty:
            self.assertEqual(len(app.metric), 0)
            self.assertEqual(len(specs), 0)
            return
        self.assertEqual(len(app.tabs[1].get("plotly_chart")), 3)
        self.assertEqual([m.value for m in app.metric], [formatar_indicador(v, esperado[v].mean()) for v in INDICADORES])
        for metric, var in zip(app.metric, INDICADORES):
            unidade = " p.p." if var == "Grad.Rate" else ""
            self.assertEqual(metric.delta, f"{esperado[var].mean() - DF[var].mean():+.1f}{unidade}")

    def test_padrao_toggle_e_metodos(self):
        app = self.app()
        self.conferir(app, DF, 5)
        app.toggle(key="separar").set_value(True).run()
        self.conferir(app, DF, 5)
        hist = [json.loads(c.proto.spec) for c in app.get("plotly_chart") if json.loads(c.proto.spec)["data"][0]["type"] == "histogram"]
        self.assertEqual(len(hist[0]["data"]), 2)
        for metodo in ["pearson", "kendall", "spearman"]:
            app.selectbox(key="metodo").set_value(metodo).run()
            self.conferir(app, DF, 5)

    def test_filtros_de_tipo_e_comparacao(self):
        app = self.app()
        for tipo in TIPOS:
            app.selectbox(key="tipo").set_value(tipo).run()
            self.conferir(app, DF[DF.Private.eq(tipo)], 5)
            self.assertTrue(any("omitidos" in c.value for c in app.caption))
        for var in INDICADORES:
            app.selectbox(key="comparar").set_value(var).run()
            self.conferir(app, DF[DF.Private.eq("Yes")], 5)

    def test_todas_as_variaveis_e_selecao_vazia(self):
        app = self.app()
        app.multiselect(key="variaveis").set_value(VARS_QUANT).run()
        self.conferir(app, DF, 17)
        app.multiselect(key="variaveis").set_value(["S.F.Ratio"]).run()
        self.conferir(app, DF, 1)
        app.multiselect(key="variaveis").set_value([]).run()
        self.conferir(app, DF, 0)

    def test_cada_slider_e_intersecao(self):
        app = self.app()
        esperado = DF
        for var in INDICADORES:
            low, high = int(DF[var].min()), int(DF[var].median())
            app.slider(key=f"intervalo_{var}").set_value((low, high)).run()
            esperado = esperado[esperado[var].between(low, high)]
            self.conferir(app, esperado, 5)

    def test_remover_variavel_remove_filtro(self):
        app = self.app()
        app.slider(key="intervalo_Apps").set_value((81, 1000)).run()
        self.conferir(app, DF[DF.Apps.between(81, 1000)], 5)
        app.multiselect(key="variaveis").set_value(["Expend"]).run()
        self.conferir(app, DF, 1)

    def test_um_registro_e_amostra_vazia(self):
        app = self.app()
        maximo = int(DF.Apps.max())
        app.slider(key="intervalo_Apps").set_value((maximo, maximo)).run()
        self.conferir(app, DF[DF.Apps.eq(maximo)], 5)
        self.assertTrue(any("insuficientes" in w.value for w in app.warning))
        app.slider(key="intervalo_Apps").set_value((81, 81)).run()
        limite = int(DF.Accept.max())
        app.slider(key="intervalo_Accept").set_value((limite, limite)).run()
        self.conferir(app, DF.iloc[:0], 0)

    def test_variavel_constante(self):
        app = self.app()
        valor = int(DF.Apps.value_counts().loc[lambda s: s.gt(1)].index[0])
        app.slider(key="intervalo_Apps").set_value((valor, valor)).run()
        self.conferir(app, DF[DF.Apps.eq(valor)], 5)
        self.assertTrue(any("constantes" in i.value for i in app.info))


if __name__ == "__main__":
    (ROOT / "tmp").mkdir(exist_ok=True)
    unittest.main()
