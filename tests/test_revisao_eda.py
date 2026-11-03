# [IA] Codex (OpenAI) - conferência independente de um exemplo conhecido de Holm.
import unittest
from scripts.conferir_entrega_final import ajustar_holm
import numpy as np


class HolmTest(unittest.TestCase):
    def test_ordem_original_e_monotonicidade(self):
        np.testing.assert_allclose(ajustar_holm([.01, .04, .03]), [.03, .06, .06])

    def test_limite_um(self):
        np.testing.assert_allclose(ajustar_holm([.9, .8]), [1, 1])
