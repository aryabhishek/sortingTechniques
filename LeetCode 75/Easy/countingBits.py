"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

https://leetcode.com/problems/counting-bits/
"""


class Solution:  # O(n log(n))
    def countBits(self, n: int) -> list[int]:
        ans = [0]
        for i in range(1, n + 1):
            count = 0
            while i > 0:
                count += i & 1
                i >>= 1
            ans.append(count)

        return ans


class Solution: # O(n)
    def countBits(self, n: int) -> list[int]:
        ans = [0]
        for i in range(1, n + 1):
            if i % 2:
                ans.append(ans[i // 2] + 1)
            else:
                ans.append(ans[i // 2])

        return ans
