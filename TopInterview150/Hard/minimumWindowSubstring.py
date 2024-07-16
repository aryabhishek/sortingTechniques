"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


class Solution: # O(n + m)
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        freq = {}
        for char in t:
            freq[char] = freq.get(char, 0) + 1

        i = j = 0
        count = 0
        min_len = float("inf")
        start = -1
        end = 0
        while j < n:
            if s[j] in freq:
                freq[s[j]] -= 1
                if freq[s[j]] >= 0:
                    count += 1

            while count == m:
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    start = i
                if s[i] in freq:
                    if freq[s[i]] == 0:
                        count -= 1
                    freq[s[i]] += 1
                i += 1

            j += 1

        return s[start : start + min_len] if start != -1 else ""
