"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.words = set(wordDict)
        self.dp = [None] * (len(s) + 1)
        return self.solve(0, s)

    def solve(self, idx, s):
        if idx == len(s):
            return True

        if self.dp[idx] is not None:
            return self.dp[idx]

        for i in range(idx + 1, len(s) + 1):
            sub_str = s[idx:i]
            if sub_str in self.words and self.solve(i, s):
                self.dp[idx] = True
                return True

        self.dp[idx] = False
        return False
