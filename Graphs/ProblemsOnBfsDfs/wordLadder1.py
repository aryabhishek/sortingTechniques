from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        word_set = set(wordList)
        word_set.discard(beginWord)

        q = deque([(beginWord, 1)])

        while q:
            word = q[0][0]
            steps = q.popleft()[1]

            if word == endWord:
                return steps

            for i in range(len(word)):

                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + char + word[i+1:]

                    if new_word in word_set:

                        word_set.remove(new_word)
                        q.append((new_word, steps+1))

        return 0
