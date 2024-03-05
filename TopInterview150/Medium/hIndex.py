"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Link: https://leetcode.com/problems/h-index/description
"""


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        n = len(citations)

        left, right = 0, n - 1

        while left <= right:

            mid = left + (right - left) // 2

            if citations[mid] == n - mid:
                return citations[mid]

            elif citations[mid] < n - mid:
                left = mid + 1

            else:
                right = mid - 1

        return n - left
