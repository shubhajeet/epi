from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    if n == 0:
        return []
    ptri = [[1]]
    for i in range(1, n):
        new = [1]
        for j in range(len(ptri[-1])-1):
            new.append(ptri[-1][j] + ptri[-1][j+1])
        new.append(1)
        ptri.append(new)

    return ptri


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
