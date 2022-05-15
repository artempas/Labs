import numpy as np
from lab6_1 import print_system, print_solution
from random import randint


def raise_max_row(matrix, current_diag_index):
    ind = current_diag_index + np.argmax(
        np.abs(matrix[current_diag_index:, current_diag_index]))  # seatching for row with max element
    if ind != current_diag_index:
        matrix[current_diag_index, :], matrix[ind, :] = np.copy(matrix[ind, :]), np.copy(
            matrix[current_diag_index, :])  # swap rows if needed


def solve_gauss(matrix):
    n = matrix.shape[0]
    # transforming matrix to triangular form
    for column in range(n - 1):
        raise_max_row(matrix, column)
        for row in range(column + 1, n):
            # modify row
            frac = matrix[row, column] / matrix[column, column]
            matrix[row, :] -= matrix[column, :] * frac

    # check modified system for nonsingularity
    if np.any(np.diag(matrix) == 0):
        return None

    solution = [0.0 for _ in range(n)]
    for column in range(n - 1, -1, -1):
        solution[column] = matrix[column, -1] / matrix[column, column]
        matrix[:, -1] -= matrix[:, column] * solution[column]
        matrix[:, column] -= matrix[:, column]

    return solution


def gauss(A, f):
    Af = np.c_[A, f]
    Af = np.array(Af, np.float64)
    solution = solve_gauss(Af)
    if solution is None:
        print("System has infinite solutions")
    return solution


if __name__ == '__main__':
    A = np.array([[randint(-9, 9) for _ in range(3)],
                  [randint(-9, 9) for _ in range(3)],
                  [randint(-9, 9) for _ in range(3)]])
    f = np.array([randint(-9, 9) for _ in range(3)])
    f = f.transpose()
    print_system(A, f)
    print_solution(gauss(A,f))
