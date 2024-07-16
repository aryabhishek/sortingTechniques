"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

from typing import List


class Solution:  # TC: (N! * N), SC: (N + N)
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.perms = []
        self.solve(nums, [], set())
        return self.perms

    def solve(self, arr, perm, taken):
        if len(perm) == len(arr):
            return self.perms.append(perm[:])

        for i in range(len(arr)):
            if arr[i] not in taken:
                perm.append(arr[i])
                taken.add(arr[i])
                self.solve(arr, perm, taken)
                taken.discard(arr[i])
                perm.pop()


class Solution:  # TC: O(N! * N), SC: O(N) auxiliary
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.perms = []
        self.solve(0, nums)
        return self.perms

    def solve(self, idx, arr):
        if idx == len(arr):
            return self.perms.append(arr[:])

        for i in range(idx, len(arr)):
            arr[idx], arr[i] = arr[i], arr[idx]
            self.solve(idx + 1, arr)
            arr[idx], arr[i] = arr[i], arr[idx]
