"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Link: https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""

        if not strs:
            return ans

        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i >= len(word) or word[i] != strs[0][i]:
                    return ans
            else:
                ans += strs[0][i]

        return ans
