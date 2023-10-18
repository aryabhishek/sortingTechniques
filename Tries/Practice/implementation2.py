class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.prefix_count = 0
        self.end_count = 0


class Trie:
    def __init__(self):
        # Write your code here.
        self.root = TrieNode()

    def insert(self, word):
        # Write your code here.
        cur = self.root
        for char in word:
            idx = ord(char) - 97
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()

            cur = cur.children[idx]
            cur.prefix_count += 1

        cur.end_count += 1

    def countWordsEqualTo(self, word):
        cur = self.root

        for char in word:
            idx = ord(char) - 97
            if cur.children[idx]:
                cur = cur.children[idx]

            else:
                return 0

        return cur.end_count

    def countWordsStartingWith(self, word):
        cur = self.root

        for char in word:
            idx = ord(char) - 97
            if cur.children[idx]:
                cur = cur.children[idx]
            else:
                return 0

        return cur.prefix_count

    def erase(self, word):
        # Write your code here.
        cur = self.root

        for char in word:
            idx = ord(char) - 97

            if cur.children[idx]:
                cur = cur.children[idx]
                cur.prefix_count -= 1

            else:
                return

        cur.end_count -= 1
