from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    odd_chars = set()
    for c in s:
        if c in odd_chars:
            odd_chars.remove(c)
        else:
            odd_chars.add(c)
    if len(s) % 2 == 0:
        return len(odd_chars) == 0
    else:
        return len(odd_chars) == 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
