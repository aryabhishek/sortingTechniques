from bisect import bisect_left
from typing import List


class Solution:  # binary Search
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [nums[0]]

        for i in range(1, n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                temp[bisect_left(temp, nums[i])] = nums[i]

        return len(temp)
