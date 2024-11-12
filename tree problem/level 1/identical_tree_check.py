class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def are_identical_trees(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return root1.value == root2.value and are_identical_trees(root1.left, root2.left) and are_identical_trees(root1.right, root2.right)


if __name__ == "__main__":
    # Example usage
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(4)

    print(f"Are the two trees identical? {are_identical_trees(root1, root2)}")