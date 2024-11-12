from queue import Queue
from collections import deque, defaultdict
from binary_tree_creation import create_binary_tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bottomView(root):

    res = []

    if root is None:
        return res

    store = defaultdict()

    q = Queue()

    q.put((root, 0))

    # BFS
    while not q.empty():
        temp = q.get()
        node , line = temp[0], temp[1]

        store[line] = node.data

        if node.left:
            q.put((node.left, line-1))

        if node.right:
            q.put((node.right, line+1))

    for key, value in sorted(store.items()):
        res.append(value)

    return res


if __name__ == '__main__':

    arr = [2 ,7 ,5 ,2 ,6 ,-1 ,9 ,-1 ,-1 ,5 ,11 ,4 ,-1]
    root = create_binary_tree(arr)

    bottom_view = bottomView(root)

    print("Bottom View:", end=" ")
    # Output each value in the
    # inorder traversal result
    for val in bottom_view:
        print(val, end=" ")
    print()