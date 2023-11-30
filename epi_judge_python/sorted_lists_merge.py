from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.
    result = None
    result_ptr = None
    L1_ptr = L1
    L2_ptr = L2
    while True:
        if L1_ptr == None and L2_ptr == None:
            return result
        elif L1_ptr == None:
            if result == None:
                result = ListNode(L2_ptr.data)
                result_ptr = result
            else:
                node = ListNode(L2_ptr.data)
                result_ptr.next = node
                result_ptr = result_ptr.next
            L2_ptr = L2_ptr.next
        elif L2_ptr == None:
            if result == None:
                result = ListNode(L1_ptr.data)
                result_ptr = result
            else:
                node = ListNode(L1_ptr.data)
                result_ptr.next = node
                result_ptr = result_ptr.next
            L1_ptr = L1_ptr.next
        elif L1_ptr.data <= L2_ptr.data:
            if result == None:
                result = ListNode(L1_ptr.data)
                result_ptr = result
            else:
                node = ListNode(L1_ptr.data)
                result_ptr.next = node
                result_ptr = result_ptr.next
            L1_ptr = L1_ptr.next
        else:
            if result == None:
                result = ListNode(L2_ptr.data)
                result_ptr = result
            else:
                node = ListNode(L2_ptr.data)
                result_ptr.next = node
                result_ptr = result_ptr.next
            L2_ptr = L2_ptr.next

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
