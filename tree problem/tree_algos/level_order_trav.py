from numpy.ma.core import left_shift

from binary_tree_creation import create_binary_tree
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order(root):

    res = []
    if root is None:
        return res

    q = deque()
    q.append(root)

    while q:
        size = len(q)
        level = []

        for i in range(size):
            node = q.popleft()
            level.append(node.data)

            if node.left:

                q.append(node.left)
            if node.right:
                q.append(node.right)

        res.append(level)
    return res


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5, 6, 7, -1, -1, 8, -1, -1, -1, 9, 10]
    root = create_binary_tree(arr)

    print(level_order(root))