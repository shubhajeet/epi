from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    # TODO - you fill in here.
    col = col.upper()
    base = 26
    col_id = 0
    for c in col:
        col_id = col_id * base + ord(c) - ord('A') + 1
    return col_id


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
