"""Esse arquivo testa o arquivo vector.py"""

import unittest  # for creating the test case
from vector import norma


class TestVectorNorma(unittest.TestCase):
    """Classe para testar a função norma no arquivo vector.py"""

    def test_norma_vazia(self):
        """Testa se a resposta é None para vetores vazios"""
        self.assertEqual(norma([]), None)

    def test_norma_1(self):
        """Testa se a resposta é correta para o vetor [1]"""
        x = [1]
        self.assertEqual(norma(x), 1)

    def test_norma_2(self):
        """Testa se a resposta é correta para o vetor [1, 2]"""
        x = [1, 2]
        self.assertAlmostEqual(norma(x), 5 ** 0.5, delta=0.01)

    def test_norma_3(self):
        """Testa se a resposta é correta para o vetor [1, 2, 3]"""
        x = [1, 2, 3]
        self.assertAlmostEqual(norma(x), 14 ** 0.5, delta=0.01)
