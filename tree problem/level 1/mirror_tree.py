class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def mirror_tree(node):
    if node is None:
        return

    mirror_tree(node.left)
    mirror_tree(node.right)

    node.left, node.right = node.right, node.left



def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.val, end=" ")
    inorder_traversal(node.right)



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Inorder traversal of the original tree:")
    inorder_traversal(root)
    print()

    # Create mirror of the tree
    mirror_tree(root)

    print("Inorder traversal of the mirror tree:")
    inorder_traversal(root)
    print()