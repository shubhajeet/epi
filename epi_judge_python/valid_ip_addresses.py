from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    # TODO - you fill in here.
    results = []
    for i in range(1, 4):
        first_part = s[:i]
        if i < len(s) and is_valid_part(first_part):
            for j in range(1, 4):
                second_part = s[i:i + j]
                if i+j < len(s) and is_valid_part(second_part):
                    for k in range(1, 4):
                        third_part = s[i + j:i + j + k]
                        if i+j+k < len(s) and is_valid_part(third_part):
                            fouth_part = s[i + j + k:]
                            if is_valid_part(fouth_part):
                                results.append(
                                    first_part + '.' + second_part + '.' + third_part + '.' + fouth_part)
    return results


def is_valid_part(s):
    return len(s) == 1 or (s[0] != '0' and int(s) <= 255)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
