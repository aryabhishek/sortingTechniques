"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
Link: https://leetcode.com/problems/subarray-sum-equals-k/
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        def solution(ind, total, k, arr):
            if ind == len(arr):
                if total == k:
                    return 1

                return 0

            total += arr[ind]
            l = solution(ind + 1, total, k, arr)
            total -= arr[ind]
            r = solution(ind + 1, total, k, arr)
            return l + r

        return solution(0, 0, k, nums)


class TopDownApproach:
    def subarraySum(self, nums: list[int], k: int) -> int:
        dp = [[-1] * (k + 1) for i in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            for j in range(k + 1):
                if i == 0:
                    dp[i][j] = 0

                if j == 0:
                    dp[i][j] = 1

        for i in range(1, len(nums) + 1):
            for j in range(1, k + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]

                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(nums)][k]


obj = TopDownApproach()
print(obj.subarraySum([1, 2, 3], 3))
