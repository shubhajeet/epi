from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    x_str = ""
    sign = "-" if x < 0 else ""
    x = abs(x)
    if x == 0:
        return "0"
    while x > 0:
        x_str = str(x % 10) + x_str
        x = int(x / 10)
    print(x_str)
    return sign + x_str


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    num = 0
    sign = 1
    s = s.upper()
    for c in s:
        if c >= '0' and c <= '9':
            num = num * 10 + int(c)
        elif c == '+':
            continue
        elif c == '-':
            sign = -1
        else:
            break
    print(num)
    return sign*num


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
