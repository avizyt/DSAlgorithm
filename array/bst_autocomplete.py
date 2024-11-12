class TreeNode:
    def __init__(self, word):
        self.word = word
        self.right = None
        self.left = None


class AutoCompleteBST:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if not self.root:
            self.root = TreeNode(word)
        else:
            self._insert_recursive(self.root, word)

    def _insert_recursive(self, node, word):
        if word < node.word:
            if node.left is None:
                node.left = TreeNode(word)
            else:
                self._insert_recursive(node.left, word)
        elif word > node.word:
            if node.right is None:
                node.left = TreeNode(word)
            else:
                self._insert_recursive(node.right, word)

    def search_prefix(self, prefix):
        result = []
        self._search_prefix_recursive(self.root, prefix, result)
        return result

    def _search_prefix_recursive(self, node, prefix, result):
        if node is not None:
            if node.word.startswith(prefix):
                result.append(node.word)
            if prefix <= node.word:
                self._search_prefix_recursive(node.left, prefix, result)
            if prefix >= node.word:
                self._search_prefix_recursive(node.right, prefix, result)


if __name__ == "__main__":
    auto_complete = AutoCompleteBST()
    words = ["apple", "app", "application", "aptitude", "banana", "band", "bandwidth"]
    for word in words:
        auto_complete.insert(word)

    print("Words with prefix 'app':", auto_complete.search_prefix("app"))
