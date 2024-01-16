from typing import List

from test_framework import generic_test
import math


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    # TODO - you fill in here.
    n = len(square_matrix)
    print(n)
    if n == 0:
        return
    half = math.ceil(n / 2)
    print(half)
    for i in range(half):
        for j in range(half):
            print((i, j))
            square_matrix[i][j], square_matrix[n - j - 1][i], square_matrix[n - i - 1][n - j - 1], square_matrix[j][
                n-i-1] = square_matrix[n - j - 1][i], square_matrix[n-i-1][n-j-1], square_matrix[j][n - i - 1], \
                square_matrix[i][j]
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
