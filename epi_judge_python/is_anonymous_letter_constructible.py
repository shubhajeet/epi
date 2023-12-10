from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # TODO - you fill in here.
    letter_text_dict = {}
    magazine_text_dict = {}
    for letter in letter_text:
        if letter in letter_text_dict:
            letter_text_dict[letter] += 1
        else:
            letter_text_dict[letter] = 1
    for letter in magazine_text:
        if letter in magazine_text_dict:
            magazine_text_dict[letter] += 1
        else:
            magazine_text_dict[letter] = 1
    for letter in letter_text_dict:
        if letter not in magazine_text_dict:
            return False
        elif letter_text_dict[letter] > magazine_text_dict[letter]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
