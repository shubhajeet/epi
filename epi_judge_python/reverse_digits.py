from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x:
        result = result * 10 + x % 10
        x //= 10
    return sign * result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
