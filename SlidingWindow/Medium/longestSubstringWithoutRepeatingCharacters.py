"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:  # My solution
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


class Solution:  # slightly optimized
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, n = 0, len(s)
        i, j = 0, 0
        seen = {}
        ans = 0

        while j < n:
            if s[j] in seen:
                if seen[s[j]] >= i:
                    i = seen[s[j]] + 1
            ans = max(ans, j - i + 1)
            seen[s[j]] = j
            j += 1

        return ans
