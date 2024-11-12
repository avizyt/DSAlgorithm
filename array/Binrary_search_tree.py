class TreeNode:
    def __init__(self, key) -> None:
        """
        Initialize a TreeNode with a specified key.

        Sets the key for the node and initializes the left and right children
        as None, indicating that the node does not have any children initially.

        :param key: The value to be assigned to the node.
        :type key: int
        """
        self.key = key
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, key):
        """
        Inserts a new node with key into the binary search tree.

        If the tree is empty, this will be the root node.
        Otherwise, it will be inserted in the correct location
        in the tree using recursive method.

        :param key: The value to be inserted into the tree.
        :type key: int
        """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """
        Recursive helper method for inserting a node with key into a Binary Search Tree.

        :param node: The current node in the tree.
        :type node: TreeNode
        :param key: The value to be inserted into the tree.
        :type key: int
        """

        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None and node.key == key:
            return node
        elif key < node.key:
            return self._search_recursive(node.left, key)
        elif key > node.key:
            return self._search_recursive(node.right, key)
        else:
            return None

    def delete(self, key):
        return self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
                # Node with two children: Get the inorder successor
                successor = self._min_value_node(node.right)
                node.key = successor.key
                node.right = self._delete_recursive(node.right, successor.key)

        return node

    def _min_value_node(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def inorder_traverse(self):
        result = []
        self._inorder_traverse_recursive(self.root, result)
        return result

    def _inorder_traverse_recursive(self, node, result):
        if node is not None:
            self._inorder_traverse_recursive(node.left, result)
            result.append(node.key)
            self._inorder_traverse_recursive(node.right, result)

    def postorder_traverse(self):
        result = []
        self._postorder_traverse_recursive(self.root, result)
        return result

    def _postorder_traverse_recursive(self, node, result):
        if node is not None:
            self._postorder_traverse_recursive(node.left, result)
            self._postorder_traverse_recursive(node.right, result)
            result.append(node.key)

    def preorder_traverse(self):
        result = []
        self._preorder_traverse_recursive(self.root, result)
        return result

    def _preorder_traverse_recursive(self, node, result):
        if node is not None:
            result.append(node.key)
            self._preorder_traverse_recursive(node.left, result)
            self._preorder_traverse_recursive(node.right, result)

    def display(self):
        """Display the BST in a structured format."""
        lines = []
        self._display_recursive(self.root, "", True, lines)
        for line in lines:
            print(line)

    def _display_recursive(self, node, prefix, is_tail, lines):
        """Helper function to recursively build the display structure."""
        if node:
            lines.append(prefix + ("└── " if is_tail else "├── ") + str(node.key))
            if node.left or node.right:
                if node.right:
                    self._display_recursive(
                        node.right,
                        prefix + ("    " if is_tail else "│   "),
                        False,
                        lines,
                    )
                if node.left:
                    self._display_recursive(
                        node.left, prefix + ("    " if is_tail else "│   "), True, lines
                    )


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(17)

    bst.display()

    print(
        "Inorder Traversal:", bst.inorder_traverse()
    )  # Sorted order: [3, 5, 7, 10, 12, 15, 17]
    print(
        "Preorder Traversal:", bst.preorder_traverse()
    )  # Root-first order: [10, 5, 3, 7, 15, 12, 17]
    print(
        "Postorder Traversal:", bst.postorder_traverse()
    )  # Left-right-root order: [3, 7, 5, 12, 17, 15, 10]

    found_node = bst.search(7)
    print("Node found:", found_node.key if found_node else "Not found")

    bst.delete(10)
    print("Inorder after deleting 10:", bst.inorder_traverse())
    bst.display()
