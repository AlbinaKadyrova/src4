import numpy as np


def euclidean_distance(x1, x2):
    """
    Вычисляет евклидово расстояние между двумя точками.
    """
    return np.sqrt(np.sum((x1 - x2) ** 2))

def manhattan_distance(x1, x2):
    """
    Вычисляет манхэттенское расстояние между двумя точками.

    """
    return np.sum(np.abs(x1 - x2))

def chebyshev_distance(x1, x2):
    """
    Вычисляет расстояние Чебышёва между двумя точками.

    """
    return np.max(np.abs(x1 - x2))



print ("euclidean_distance",euclidean_distance( 10,5))
print("manhattan_distance",manhattan_distance(10,5))
print("chebyshev_distance",chebyshev_distance(10,5))