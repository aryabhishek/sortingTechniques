class TrieNode:
    def __init__(self):
        self.children = [None] * 26

    def contains_key(self, char) -> bool:
        return self.children[ord(char) - 97]

    def put(self, char, node) -> None:
        self.children[ord(char) - 97] = node

    def get(self, char):
        return self.children[ord(char) - 97]


def countDistinctSubstrings(s):
    # Write your code here

    root = TrieNode()
    ans = 0

    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            if not node.contains_key(s[j]):
                ans += 1
                node.put(s[j], TrieNode())

            node = node.get(s[j])

    return ans + 1
