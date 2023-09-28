from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        
        word_set = set(wordList)
        q = deque([beginWord])
        used_on_level = [beginWord]

        level = 0
        ans = []

        while q:
            temp_arr = q.popleft()
            if len(temp_arr) > level:
                level += 1
                for item in used_on_level:
                    word_set.discard(item)
                used_on_level.clear()

            word = temp_arr[-1] # last word of current path

            if word == endWord:
                if not ans:
                    ans.append(temp_arr)
                elif len(ans[0]) == len(temp_arr):
                    ans.append(temp_arr)

            for i in range(len(word)):

                for char in "abcdefghijklmnopqrstuvwxyz":
                    n_word = word[:i] + char + word[i+1:]
                    if n_word in word_set:
                        temp_arr.append(n_word)
                        q.append(temp_arr)
                        used_on_level.append(n_word)
                        temp_arr.pop()

        return ans