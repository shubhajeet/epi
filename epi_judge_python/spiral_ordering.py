from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    start = 0
    end = len(square_matrix) - 1
    ans = []
    while start <= end:
        # top
        for i in range(start, end+1):
            ans.append(square_matrix[start][i])
            # print(square_matrix[start][i])
        # right
        for i in range(start+1, end+1):
            ans.append(square_matrix[i][end])
            # print(square_matrix[i][end])
        # bottom
        for i in range(end-1, start-1, -1):
            ans.append(square_matrix[end][i])
            # print(square_matrix[end][i])
        # left
        for i in range(end-1, start, -1):
            ans.append(square_matrix[i][start])
            # print(square_matrix[i][start])
        start += 1
        end -= 1
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
