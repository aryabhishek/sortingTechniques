"""
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

https://leetcode.com/problems/maximum-subsequence-score/
"""

from heapq import heappop, heappush


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n = len(nums1)

        both_nums = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)

        min_heap = []
        k_sum = 0

        for i in range(k):
            k_sum += both_nums[i][0]
            heappush(min_heap, both_nums[i][0])

        res = k_sum * both_nums[k - 1][1]

        for i in range(k, n):
            k_sum += both_nums[i][0]
            heappush(min_heap, both_nums[i][0])

            k_sum -= heappop(min_heap)

            res = max(res, k_sum * both_nums[i][1])

        return res
