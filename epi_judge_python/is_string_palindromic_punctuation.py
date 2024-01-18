from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    front_idx = 0
    back_idx = len(s) - 1
    while front_idx < back_idx:
        if not s[front_idx].isalnum():
            front_idx += 1
            continue
        if not s[back_idx].isalnum():
            back_idx -= 1
            continue
        if s[front_idx].lower() != s[back_idx].lower():
            return False
        front_idx += 1
        back_idx -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
