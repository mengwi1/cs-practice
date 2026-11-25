import numpy as np


def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    m = np.array(matrix)
    return m[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    m = np.array(matrix).copy()
    m[row_start:row_stop, column_start:column_stop] = value
    return m.tolist()


def matrix_vector_product(matrix, vector):
    return (np.array(matrix) @ np.array(vector)).tolist()


def matrix_multiply(left, right):
    return (np.array(left) @ np.array(right)).tolist()

def transpose_matrix(matrix):
    return np.array(matrix).T.tolist()

def solve_system(matrix, vector):
    x = np.linalg.solve(np.array(matrix, dtype=float), np.array(vector, dtype=float))
    return np.round(x, 6).tolist()

def tensor_channel_mean(tensor):
    return np.array(tensor).mean(axis=-1).tolist()

def point_distance(first, second):
    d = np.linalg.norm(np.array(first, dtype=float) - np.array(second, dtype=float))
    return round(float(d), 6)