"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""


from typing import List

class TrieNode:
    def __init__(self, word="", is_end=False):
        self.word = word
        self.is_end = is_end
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        crawler = self.root

        for char in word:
            idx = ord(char) - 97
            if crawler.children[idx] is None:
                crawler.children[idx] = TrieNode()
            crawler = crawler.children[idx]
        crawler.is_end = True
        crawler.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        self.res = []
        self.dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        trie = Trie()

        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                char = board[i][j]
                idx = ord(char) - 97

                if trie.root.children[idx] is not None:
                    self.search(i, j, m, n, board, trie.root)

        return self.res

    def search(self, i, j, m, n, board, root):
        if i < 0 or i >= m or j < 0 or j >= n:
            return

        char = board[i][j]
        idx = ord(char) - 97

        if char == "$" or root.children[idx] is None:
            return

        root = root.children[idx]

        if root.is_end:
            self.res.append(root.word)
            root.is_end = False

        temp, board[i][j] = board[i][j], "$"

        for dx, dy in self.dir:
            self.search(i + dx, j + dy, m, n, board, root)

        board[i][j] = temp


if __name__ == "__main__":
    s = Solution()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]

    print(s.findWords(board, words))
