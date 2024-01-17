from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    # TODO - you fill in here.
    half = len(s) // 2
    for i in range(half):
        if s[i] != s[-(i+1)]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
