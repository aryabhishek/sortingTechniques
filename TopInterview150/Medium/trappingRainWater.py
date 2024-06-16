"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, arr: list[int]) -> int:
        n = len(arr)
        max_left = [arr[0]] * n
        max_right = [arr[-1]] * n

        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], arr[i])

        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], arr[i])

        water = [min(max_left[i], max_right[i]) - arr[i] for i in range(n)]

        return sum(water)
