from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.'
    # pos = {i: i for i in range(len(A))}
    # copyarr = []
    # for i in range(len(perm)):
    #     copyarr.append(A[perm[i]])
    # print(copyarr)
    # A = copyarr
    # print(A)
    # for i in range(len(perm)):
    #     acutual_pos = pos[perm[i]]
    #     A[i], A[acutual_pos] = A[acutual_pos], A[i]
    #     pos[acutual_pos] = i
    #     pos[i] = acutual_pos
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            tmp = perm[next]
            perm[next] = perm[next] - len(perm)
            next = tmp
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
