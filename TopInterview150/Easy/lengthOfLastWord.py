"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Link: https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        char_len = 0
        space_len = 0
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] == " ":
                if char_len:
                    return char_len
                space_len += 1

            else:
                char_len += 1

        return char_len
