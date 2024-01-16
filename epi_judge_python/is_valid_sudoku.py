from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    box = [[set() for _ in range(3)] for _ in range(3)]
    for i in range(9):
        for j in range(9):
            # row check
            if partial_assignment[i][j] == 0:
                continue
            if partial_assignment[i][j] in row[i]:
                return False
            else:
                row[i].add(partial_assignment[i][j])
            # col check
            if partial_assignment[i][j] in col[j]:
                return False
            else:
                col[j].add(partial_assignment[i][j])

            if partial_assignment[i][j] in box[i//3][j//3]:
                return False
            else:
                box[i//3][j//3].add(partial_assignment[i][j])
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
