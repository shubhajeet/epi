import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import math


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # TODO - you fill in here.
    # print(s)

    def reverse(start, end):
        for i in range(int((end-start)/2)):
            s[start+i], s[end-1-i] = s[end-1-i], s[start+i]
    front_word = 0
    front_word_len = 0
    last_word = len(s)
    last_word_len = 0
    for i in range(math.ceil(len(s)/2)):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        if s[i] == ' ':
            reverse(front_word, front_word+front_word_len)
            front_word_len = 0
            front_word = i+1
        else:
            front_word_len += 1
        if s[len(s)-1-i] == ' ':
            reverse(last_word-last_word_len, last_word)
            last_word_len = 0
            last_word = len(s)-1-i
        else:
            last_word_len += 1
    # print(s)
    # print(i)

    reverse(front_word, last_word)
    # print(s)
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
