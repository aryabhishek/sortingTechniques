"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

https://leetcode.com/problems/maximal-rectangle/
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        row = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    row[j] += 1
                else:
                    row[j] = 0
            ans = max(ans, self.largestRectangleArea(row))
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
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
