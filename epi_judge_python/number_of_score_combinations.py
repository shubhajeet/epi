from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # TODO - you fill in here.

    dp = {}

    def num_combination(score):
        if score in dp:
            return dp[score]
        if score == 0:
            return 1
        if score < 0:
            return 0
        dp[score] = sum(num_combination(score - s)
                        for s in individual_play_scores)
        return dp[score]
    comb = num_combination(final_score)
    print(comb)
    print(dp)
    return comb


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
