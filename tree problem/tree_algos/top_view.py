
from collections import deque, defaultdict
from binary_tree_creation import create_binary_tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def topView(root):

    res = []

    if root is None:
        return res

    store = defaultdict()

    q = deque()

    q.append((root, 0))

    # BFS
    while q:
        node , line = q.popleft()

        if line not in store:
            store[line] = node.data

        if node.left:
            q.append((node.left, line-1))

        if node.right:
            q.append((node.right, line+1))

    for key,value in sorted(store.items()):
        res.append(value)

    return res


if __name__ == '__main__':

    arr = [2 ,7 ,5 ,2 ,6 ,-1 ,9 ,-1 ,-1 ,5 ,11 ,4 ,-1]
    root = create_binary_tree(arr)

    bottom_view = topView(root)

    print("Bottom View:", end=" ")
    # Output each value in the
    # inorder traversal result
    for val in bottom_view:
        print(val, end=" ")
    print()