"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

https://leetcode.com/problems/largest-rectangle-in-histogram/
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                ele = stack.pop()
                nse = i
                pse = stack[-1] if stack else -1

                max_area = max(max_area, heights[ele] * (nse - pse - 1))
            stack.append(i)
        nse = n
        while stack:
            ele = stack.pop()
            pse = stack[-1] if stack else -1
            max_area = max(max_area, heights[ele] * (nse - pse - 1))

        return max_area
