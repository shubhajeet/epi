from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    # TODO - you fill in here.
    dp = {}

    def has_two_sum(t: int) -> bool:
        if t in dp:
            return dp[t]
        prev = set()
        for a in A:
            prev.add(a)
            if t - a in prev:
                dp[t] = True
                return True
        dp[t] = False
        return False

    for a in A:
        if has_two_sum(t - a):
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
