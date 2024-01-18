from test_framework import generic_test


def look_and_say(n: int) -> str:
    # TODO - you fill in here.
    # if n == 0:
    #     return ""
    s = "1"
    for _ in range(n-1):
        s = next_number(s)
        # print(s)
    return s


def next_number(s):
    result = ""
    index = 0
    while index < len(s):
        count = 1
        while index < len(s)-1 and s[index] == s[index+1]:
            count += 1
            index += 1
        result += str(count) + s[index]
        index += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
