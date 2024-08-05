"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

https://leetcode.com/problems/kth-largest-element-in-an-array
"""

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return min(nums)

        heap = []
        heapq.heapify(heap)

        for i in range(k):
            heapq.heappush(heap, nums[i])

        for i in range(k, n):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])

        return heap[0]
