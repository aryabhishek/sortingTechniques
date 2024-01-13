"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Link: https://leetcode.com/problems/longest-consecutive-sequence/
"""


class Solution:
    def longestConsecutive(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        a_set = set(arr)

        ans = 1

        for it in a_set:
            if it - 1 not in a_set:
                x = it + 1
                count = 1

                while x in a_set:
                    x += 1
                    count += 1

                ans = max(ans, count)

        return ans
