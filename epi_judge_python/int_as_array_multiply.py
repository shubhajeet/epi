from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    result = [0 for i in range(len(num1) + len(num2))]
    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j + 1] += abs(num1[i] * num2[j])
    for i in reversed(range(len(result))):
        if result[i] >= 10:
            result[i - 1] += result[i] // 10
            result[i] %= 10
    for i in range(len(result)):
        if result[i] != 0:
            break
    result = result[i:]
    if num1[0] * num2[0] < 0:
        result[0] *= -1
    # print(result)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
