"""Módulo com as funções de manipulação de vetores."""


def norma(x: list[float]) -> float | None:
    """Calcula a norma de um vetor"""
    # TODO: implementar
    # a norma de um vetor [3, 4] é 5
    # a norma de um vetor [1, 2, 4] é 4.58257569495584
    # ela consiste em calcular a raiz quadrada da soma dos quadrados dos elementos do vetor
    # se o vetor estiver vazio retorne None


def soma(x: list[float], y: list[float]) -> list[float] | None:
    """Soma dois vetores"""
    # TODO: implementar
    # a soma de dois vetores [1, 2, 4] + [2, 3, 4] é [3, 5, 8]
    # a soma só pode ser realizada se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None


def multiplicação_por_escalar(vetor: list[float], escalar: float) -> list[float]:
    """Multiplica um vetor por um escalar"""
    # TODO: implementar
    # a multiplicação de um vetor [1, 2, 4] por um escalar 2 é [2, 4, 8]


def produto_interno(x: list[float], y: list[float]) -> float | None:
    """Calcula o produto interno de dois vetores"""
    # TODO: implementar
    # o produto interno de dois vetores [1, 2, 4] e [2, 3, 4] é 24
    # o produto interno consiste em multiplicar os elementos de mesmo índice e somar os resultados
    # a multiplicação só pode ser realizada se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None
    # caso os vetores sejam vazios o resultado é 0


def produto_vetorial(x: list[float], y: list[float]) -> list[float] | None:
    """Calcula o produto vetorial de dois vetores"""
    # TODO: implementar
    # o produto vetorial de dois vetores [1, 2, 4] e [2, 3, 4] é [-4, 4, -1]
    # o produto vetorial só pode ser realizado se os vetores tem 3 elementos.
    # caso contrário, deve retornar None


def produto_diádico(x: list[float], y: list[float]) -> list[list[float]] | None:
    """Calcula o produto diádico de dois vetores"""
    # TODO: implementar
    # o produto diádico de dois vetores [1, 2, 4] e [2, 3, 4] é [[2, 3, 4], [4, 6, 8], [8, 12, 16]]
    # o produto diádico só pode ser realizado se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None
