from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    def max(tree):
        if tree.right:
            return max(tree.right)
        else:
            return tree.data

    def min(tree):
        if tree.left:
            return min(tree.left)
        else:
            return tree.data

    def check_bst(tree):
        cond = True
        if tree is None:
            return True
        if tree.left:
            if max(tree.left) > tree.data:
                return False
            else:
                cond = cond and check_bst(tree.left)
        if tree.right:
            if min(tree.right) < tree.data:
                return False
            else:
                cond = cond and check_bst(tree.right)
        return cond
    return check_bst(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
