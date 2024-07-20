"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []

        self.digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        self.combinations = []
        self.solve(0, digits, [])
        return self.combinations

    def solve(self, idx, s, temp):
        if idx == len(s):
            self.combinations.append("".join(temp))
            return
        char = self.digit_to_letters[s[idx]]
        for letter in char:
            self.solve(idx + 1, s, temp + [letter])
