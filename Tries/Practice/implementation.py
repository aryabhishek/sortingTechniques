class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        start = self.root
        for char in word:
            idx = ord(char) - 97
            if start.children[idx] is None:
                start.children[idx] = TrieNode()
            start = start.children[idx]

        start.isEnd = True

    def search(self, word) -> bool:
        start = self.root

        for char in word:
            if start.children[ord(char) - 97] is None:
                return False
            start = start.children[ord(char) - 97]

        return start.isEnd

    def startsWith(self, word):
        start = self.root

        for char in word:
            if start.children[ord(char) - 97] is None:
                return False
            start = start.children[ord(char) - 97]

        return True


obj = Trie()

obj.insert("abc")
obj.insert("hello")
obj.insert("nigga")


if obj.startsWith("n"):
    obj.insert("sekrio")

print(obj.search("sekiro"))
