"""Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
Link: https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(pattern) != len(s):
            return False

        dic = {}

        for i, j in zip(pattern, s):
            if i in dic and j != dic[i]:
                return False
            dic[i] = j
            if len(set(dic.values())) != len(set(dic.keys())):
                return False

        return True
