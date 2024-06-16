"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    def maxArea(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1
        max_area = 0

        while left < right:
            height = min(arr[left], arr[right])
            width = right - left
            max_area = max(max_area, height * width)

            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return max_area
