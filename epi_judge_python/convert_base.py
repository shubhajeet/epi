from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    is_negative = num_as_string[0] == '-'
    num_as_string = num_as_string.upper()
    b2_string = ''
    if is_negative:
        num_as_string = num_as_string[1:]
    num = 0
    for c in num_as_string:
        if c.isalpha():
            num = num * b1 + ord(c) - ord('A') + 10
        else:
            num = num * b1 + int(c)
    while num:
        digit = num % b2
        if digit >= 10:
            b2_string = chr(ord('A') + digit - 10) + b2_string
        else:
            b2_string = str(digit) + b2_string
        num //= b2
    if is_negative:
        b2_string = '-' + b2_string
    if b2_string == '':
        b2_string = '0'
    return b2_string


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
