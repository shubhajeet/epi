import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    # TODO - you fill in here.
    # print(task_durations)
    sorted_task_durations = [(task_durations[i], i)
                             for i in range(len(task_durations))]
    sorted_task_durations.sort()
    paired_tasks = []
    for i in range(len(task_durations) // 2):
        paired_tasks.append(PairedTasks(
            sorted_task_durations[i][0], sorted_task_durations[-i - 1][0]))
    return paired_tasks


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
