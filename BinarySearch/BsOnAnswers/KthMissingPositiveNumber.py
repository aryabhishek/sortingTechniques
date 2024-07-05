"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.
"""


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k


class OptimizedSolution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2
            missing = arr[mid] - mid - 1
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k
