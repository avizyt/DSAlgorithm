class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height_of_binary_tree(node):
    """
    Base Case
    :param Node: None
    :return: -1
    """
    if node is None:
        return -1

    # Recur for left and right tree and take the maximum of both
    left_height = height_of_binary_tree(node.left)
    right_height = height_of_binary_tree(node.right)

    # Return the height
    return max(left_height, right_height) + 1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(f"Height of the binary tree is: {height_of_binary_tree(root)}")
