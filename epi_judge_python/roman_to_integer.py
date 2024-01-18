from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    # TODO - you fill in here.
    roman_values = {"I": (0, 1), "V": (1, 5), "X": (2, 10), "L": (
        3, 50), "C": (4, 100), "D": (5, 500), "M": (6, 1000)}
    roman_char = ["I", "V", "X", "L", "C", "D", "M", None, None]
    num = 0
    for i in range(len(s)):
        if i < len(s)-1 and (s[i+1] == roman_char[roman_values[s[i]][0]+1] or s[i+1] == roman_char[roman_values[s[i]][0]+2]):
            num -= roman_values[s[i]][1]
        else:
            num += roman_values[s[i]][1]
    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
