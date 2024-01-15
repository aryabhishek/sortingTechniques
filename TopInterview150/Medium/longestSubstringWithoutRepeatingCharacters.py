"""
Given a string s, find the length of the longest 
substring without repeating characters.
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, n = 0, len(s)
        i, j = 0, 0
        mp = set()
        k = 0

        while j < n:
            if s[j] in mp:
                mp.discard(s[i])
                i += 1
                k -= 1
            else:
                k += 1
                mp.add(s[j])
                j += 1
            ans = max(ans, k)

        return ans
