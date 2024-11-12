
from collections import deque, defaultdict
from binary_tree_creation import create_binary_tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findVertical(root):
    nodes = defaultdict(lambda: defaultdict(lambda : set()))

    # (node, (vertical, level))
    todo = deque([(root, (0, 0))])

    while todo:
        temp , (x, y) = todo.popleft()

        nodes[x][y].add(temp.data)

        if temp.left:
            todo.append((temp.left, (x-1, y+1)))

        if temp.right:
            todo.append((temp.right, (x+1, y+1)))

    res = []
    for x, y_vals in nodes.items():
        col = []
        for y, val in y_vals.items():
            col.extend(sorted(val))
        res.append(col)
    return res

def printResult(result):
    for level in result:
        for node in level:
            print(node, end=" ")
        print()
    print()


if __name__ == '__main__':
    arr = [2, 7, 5, 2, 6, -1, 9, -1, -1, 5, 11, 4, -1]
    arr2 = [1,2,3,4,10,9,11,-1,-1,-1,-1,-1,-1, -1,6]
    root = create_binary_tree(arr2)

    vertical_view = findVertical(root)

    print("Vertical Traversal View:\n")
    print(vertical_view)

    # printResult(vertical_view)