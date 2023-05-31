"""Esse arquivo testa o arquivo vector.py"""

import unittest  # for creating the test case
from vector import produto_diádico as prod


class TestVectorProdutoDiádico(unittest.TestCase):
    """Classer para testar a função produto_diádico no arquivo vector.py"""

    def test_produto_diádico_vazio(self):
        """Testa se a resposta é vazia para vetores vazios"""
        self.assertEqual(prod([], []), [])

    def test_produto_diádico_incompatível(self):
        """Testa se a resposta é None para vetores de tamanhos diferentes"""
        self.assertEqual(prod([1, 2], [1]), None)

    def test_produto_diádico_1(self):
        """Testa se a resposta é correta para os vetores [1] e [2]"""
        x = [1]
        y = [2]
        self.assertEqual(prod(x, y), [[2]])

    def test_produto_diádico_2(self):
        """Testa se a resposta é correta para os vetores [1, 2] e [2, 3]"""
        x = [1, 2]
        y = [2, 3]
        self.assertEqual(prod(x, y), [[2, 3], [4, 6]])

    def test_produto_diádico_3(self):
        """Testa se a resposta é correta para os vetores [1, 2, 3] e [2, 3, 4]"""
        x = [1, 2, 3]
        y = [2, 3, 4]
        self.assertEqual(prod(x, y), [[2, 3, 4], [4, 6, 8], [6, 9, 12]])

    def test_produto_diádico_4(self):
        """Testa se a resposta é correta para os vetores [1, 2, 3, 4] e [2, 3, 4, 5]"""
        x = [1, 2, 3, 4]
        y = [2, 3, 4, 5]
        self.assertEqual(prod(x, y), [[2, 3, 4, 5], [4, 6, 8, 10], [
            6, 9, 12, 15], [8, 12, 16, 20]])
