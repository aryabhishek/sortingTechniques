"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations = []
        self.solve(1, n, k, [])
        return self.combinations

    def solve(self, start, n, k, temp):
        if k == 0:
            return self.combinations.append(temp)

        if start > n:
            return

        self.solve(start + 1, n, k - 1, temp + [start])  # take current element
        self.solve(start + 1, n, k, temp)  # skip current element
