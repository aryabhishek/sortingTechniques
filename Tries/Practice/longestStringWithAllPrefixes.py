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

    def isPrefix(self, word):
        cur = self.root
        flag = True
        for char in word:
            if not flag:
                break

            if cur.children[ord(char) - 97] is not None:
                cur = cur.children[ord(char) - 97]
                if not cur.isEnd:
                    return False
            else:
                return False

        return True

# main
def completeString(n: int, a: list[str]) -> str:
    # Write your Code here
    storage = Trie()

    for word in a:
        storage.insert(word)

    longest = ""

    for word in a:
        if storage.isPrefix(word):
            if len(word) > len(longest):
                longest = word
            elif len(word) == len(longest) and word < longest:
                longest = word

    if longest == "":
        return "None"
    return longest
