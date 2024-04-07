class TreeNode:

    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:

        curr = self.root

        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TreeNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:

        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if not curr.children[i]:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:
            i = ord(c) - ord("a")

            if curr.children[i] == None:
                return False
            curr = curr.children[i]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
