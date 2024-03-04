"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Link: https://leetcode.com/problems/group-anagrams
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = defaultdict(list)

        for word in strs:
            key = self.generate(word)
            mp[key].append(word)

        return list(mp.values())

    def generate(self, word):
        arr = [0] * 26

        for char in word:
            arr[ord(char) - ord("a")] += 1

        return tuple(arr)  # tuples are immutable
