"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

https://leetcode.com/problems/combination-sum-iii
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        self.res = []
        self.k = k
        self.n = n
        self.solve(1, 0, [])
        return self.res

    def solve(self, num, cur_sum, temp):
        if len(temp) == self.k:
            if cur_sum == self.n:
                self.res.append(temp)
            return

        for i in range(num, 10):
            self.solve(i + 1, cur_sum + i, temp + [i])
