"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        start = self.root
        for char in word:
            idx = ord(char) - 97
            if start.children[idx] is None:
                start.children[idx] = TrieNode()
            start = start.children[idx]

        start.isEnd = True

    def search(self, word, start=None) -> bool:
        if start is None:
            start = self.root

        for idx, char in enumerate(word):
            if char == ".":
                for i in range(26):
                    if start.children[i] is not None:
                        if self.search(word[idx + 1 :], start.children[i]):
                            return True
                return False
            else:
                idx_char = ord(char) - ord("a")
                if start.children[idx_char] is None:
                    return False
                start = start.children[idx_char]

        return start.isEnd
