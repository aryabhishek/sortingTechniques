"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Link: https://leetcode.com/problems/implement-trie-prefix-tree
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        start = self.root
        for char in word:
            idx = ord(char) - 97
            if start.children[idx] is None:
                start.children[idx] = TrieNode()
            start = start.children[idx]

        start.isEnd = True

    def search(self, word: str) -> bool:
        start = self.root

        for char in word:
            if start.children[ord(char) - 97] is None:
                return False
            start = start.children[ord(char) - 97]

        return start.isEnd

    def startsWith(self, prefix: str) -> bool:
        start = self.root

        for char in prefix:
            if start.children[ord(char) - 97] is None:
                return False
            start = start.children[ord(char) - 97]

        return True
