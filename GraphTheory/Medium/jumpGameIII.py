"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

https://leetcode.com/problems/jump-game-iii/
"""


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        vis = [0] * n
        self.arr = arr

        def solve(i):
            if i >= n or i < 0:
                return False

            if self.arr[i] == 0:
                return True

            if vis[i] == 1:
                return False

            vis[i] = 1
            return solve(i + self.arr[i]) or solve(i - self.arr[i])

        return solve(start)
