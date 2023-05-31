"""Esse arquivo testa o arquivo matrix.py"""

import unittest  # for creating the test case
from matrix import é_simétrica


class TestMatrixÉSimétrica(unittest.TestCase):
    """Classe para testar a função é_simétrica no arquivo matrix.py"""

    def test_é_simétrica_vazia(self):
        """Testa se a resposta é True para matrizes vazias"""
        self.assertEqual(é_simétrica([]), True)

    def test_é_simétrica_1x1(self):
        """Testa se a resposta é True para a matriz [[1]]"""
        x = [[1]]
        self.assertEqual(é_simétrica(x), True)

    def test_é_simétrica_2x2(self):
        """Testa se a resposta é True para a matriz [[1, 2], [2, 1]]"""
        x = [[1, 2],
             [2, 1]]
        self.assertEqual(é_simétrica(x), True)

    def test_é_simétrica_2x2_false(self):
        """Testa se a resposta é False para a matriz [[1, 3], [2, 3]]"""
        x = [[1, 3],
             [2, 3]]
        self.assertEqual(é_simétrica(x), False)

    def test_é_simétrica_3x3(self):
        """Testa se a resposta é True para a matriz [[1, 2, 4], [2, 3, 4], [4, 4, 4]]"""
        x = [[1, 2, 4],
             [2, 3, 4],
             [4, 4, 4]]
        self.assertEqual(é_simétrica(x), True)

    def test_é_simétrica_3x3_false(self):
        """Testa se a resposta é False para a matriz [[1, 2, 1], [2, 3, 4], [1, 2, 4]]"""
        x = [[1, 2, 1],
             [2, 3, 4],
             [1, 2, 4]]
        self.assertEqual(é_simétrica(x), False)
