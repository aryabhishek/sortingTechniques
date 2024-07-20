"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        start = 0
        self.memo = [[-1] * n for i in range(n)]

        for i in range(n):
            for j in range(i, n):
                if self.is_palin(i, j, s) and max_len < j - i + 1:
                    max_len = j - i + 1
                    start = i

        return s[start : start + max_len]

    def is_palin(self, i, j, s):
        if i >= j:
            return 1

        if self.memo[i][j] != -1:
            return 1

        if s[i] == s[j]:
            self.memo[i][j] = self.is_palin(i + 1, j - 1, s)
            return self.memo[i][j]

        self.memo[i][j] = 0
        return 0
