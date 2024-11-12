from binary_tree_creation import create_binary_tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_path(root, path, target):

    if root is None:
        return 

    path.append(root.data)

    if root.data == target and root.left is None and root.right is None:
        return path

    left_path = find_path(root.left, path, target)
    if left_path:
        return left_path

    right_path = find_path(root.right, path, target)
    if right_path:
        return right_path

    return []



def getPath(root, arr, target):
    if not root:
        return False

    arr.append(root.data)

    if root.data == target:
        return True

    if getPath(root.left, arr, target) or getPath(root.right, arr, target):
        return True

    arr.pop()
    return False

def path(root, target):

    arr = []

    if not root:
        return arr

    find_path(root, arr, target)

    return arr

if __name__ == '__main__':

    arr = [1, 2, 3, -1, -1, 4, 5, -1, -1, 6]
    arr2 = [1,2,3,4,10,9,11,-1,-1,-1,-1,-1,-1, -1,6]
    root = create_binary_tree(arr)

    target_leaf = 6
    solution_path = path(root, target_leaf)

    print(f"Path from root to leaf with value {target_leaf}: \n")
    print(solution_path)



