"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        count = ans = sum(1 for i in range(k) if s[i] in vowels)

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            ans = max(ans, count)

        return ans
