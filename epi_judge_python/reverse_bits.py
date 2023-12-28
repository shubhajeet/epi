from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    reverse = 0
    for _ in range(64):
        reverse = reverse << 1
        reverse = reverse | (x & 1)
        x = x >> 1
    return reverse


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
