class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_level_order(arr, root, i, n):
    """
    Function to insert elements in level order into a binary tree.
    :param arr: List of numbers
    :param root: Current node
    :param i: Current index in the array
    :param n: Size of the array
    :return: The constructed binary tree's root node
    """
    # Base case for recursion
    if i < n and arr[i] != -1:
        temp = Node(arr[i])
        root = temp

        # Insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # Insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)

    return root


def create_binary_tree(arr):
    """
    Automates the binary tree creation process from an array of numbers.
    :param arr: List of numbers
    :return: Root of the binary tree
    """
    n = len(arr)
    if n == 0:
        return None
    return insert_level_order(arr, None, 0, n)


# Example usage
arr = [1, 2, 3, 4, 5]
root = create_binary_tree(arr)

# The tree created will have the same structure as:
#        1
#      /   \
#     2     3
#    / \
#   4   5
