from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    max_depth = None
    min_depth = None

    def traverse(node, depth):
        # check if node is leaf
        nonlocal max_depth, min_depth
        if node.left == None and node.right == None:
            # print(depth)
            if max_depth == None:
                max_depth = depth
            elif depth > max_depth:
                max_depth = depth
            if min_depth == None:
                min_depth = depth
            elif depth < min_depth:
                min_depth = depth
            if max_depth != None and min_depth != None:
                if (max_depth - min_depth) <= 1:
                    # print("True")
                    return True
                else:
                    # print("False")
                    return False
            # print("True")
            return True
        answer = True
        if node.left != None:
            answer = traverse(node.left, depth + 1)
        if answer == False:
            return False
        if node.right != None:
            answer = traverse(node.right, depth + 1)
        return answer
    return traverse(tree, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
