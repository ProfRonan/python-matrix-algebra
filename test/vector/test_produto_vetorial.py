"""Esse arquivo testa o arquivo vector.py"""

import unittest  # for creating the test case
from vector import produto_vetorial as prod_vet


class TestVectorProdutoVetorial(unittest.TestCase):
    """Classe para testar a função produto_vetorial no arquivo vector.py"""

    def test_produto_vetorial_vazia(self):
        """Testa se a resposta é None para vetores vazios"""
        self.assertEqual(prod_vet([], []), None)

    def test_produto_vetorial_incompatível(self):
        """Testa se a resposta é None para vetores incompatíveis"""
        x = [1, 2]
        y = [1, 2, 3]
        self.assertEqual(prod_vet(x, y), None)

    def test_produto_vetorial_3(self):
        """Testa se a resposta é correta para os vetores [1, 2, 3] e [2, 3, 4]"""
        x = [1, 2, 4]
        y = [2, 3, 4]
        self.assertEqual(prod_vet(x, y), [-4, 4, -1])

    def test_produto_vetorial_3_2(self):
        """Testa se a resposta é correta para os vetores [0, 0, 0] e [2, 3, 4]"""
        x = [0, 0, 0]
        y = [2, 3, 4]
        self.assertEqual(prod_vet(x, y), [0, 0, 0])

    def test_produto_vetorial_3_3(self):
        """Testa se a resposta é correta para os vetores [2, 3, 4] e [1, 2, 3]"""
        x = [2, 3, 4]
        y = [1, 2, 3]
        self.assertEqual(prod_vet(x, y), [1, -2, 1])
