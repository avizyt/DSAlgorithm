from binary_tree_creation import create_binary_tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_trav(root, arr):
    if root is None:
        return

    arr.append(root.data)
    preorder_trav(root.left, arr)
    preorder_trav(root.right, arr)



def preorder(root):
    arr = []
    preorder_trav(root, arr)
    return arr

if __name__ == "__main__":
    # Creating a sample binary tree
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    #
    # # Getting inorder traversal
    # result = preorder(root)

    arr = [1, 2, 3, 4, 5]
    root = create_binary_tree(arr)
    # Getting inorder traversal
    result = preorder(root)

    # Displaying the inorder traversal result
    print("Preorder Traversal:", end=" ")
    # Output each value in the
    # inorder traversal result
    for val in result:
        print(val, end=" ")
    print()