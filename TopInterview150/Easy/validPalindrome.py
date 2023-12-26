"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
Link: https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = "".join(filter(str.isalnum, s))

        return self.check_palin(ans.lower(), 0)

    def check_palin(self, s: str, idx: int) -> bool:
        if idx >= len(s):
            return True

        if s[idx] != s[len(s) - idx - 1]:
            return False

        return self.check_palin(s, idx + 1)
