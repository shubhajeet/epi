from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    if x < 0:
        return False
    digits = []
    while x:
        digits.append(x % 10)
        x //= 10
    for i in range(len(digits) // 2):
        if digits[i] != digits[-i - 1]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
