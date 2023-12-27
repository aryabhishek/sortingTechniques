"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

Link: https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        return True
