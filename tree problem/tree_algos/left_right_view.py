from binary_tree_creation import create_binary_tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftview(root, level, res):
    if root is None:
        return

    if len(res) == level:
        res.append(root.data)
    leftview(root.left, level+1, res)
    leftview(root.right, level+1, res)

def left_viewer(root):
    res = []
    leftview(root,0, res)
    return res

def rightview(root, level, res):
    if root is None:
        return

    if len(res) == level:
        res.append(root.data)
    rightview(root.right, level+1, res)
    rightview(root.left, level+1, res)

def right_viewer(root):
    res = []
    rightview(root,0, res)
    return res



if __name__ == '__main__':
    # arr = [1, 2, 3, -1, 4, 5]
    arr = [2, 7, 5, 2, 6, -1, 9, -1, -1, 5, 11, 4, -1]
    root = create_binary_tree(arr)
    # Getting inorder traversal
    left_side = left_viewer(root)
    right_side = right_viewer(root)

    # Displaying the inorder traversal result
    print("Left View:", end=" ")
    # Output each value in the
    # inorder traversal result
    for val in left_side:
        print(val, end=" ")
    print()

    print("Right View:", end=" ")
    # Output each value in the
    # inorder traversal result
    for val in right_side:
        print(val, end=" ")
    print()
