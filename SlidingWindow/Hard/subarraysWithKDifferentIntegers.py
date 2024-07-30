"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
"""

from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k) - self.helper(nums, k - 1)

    def helper(self, nums, k):
        freq = defaultdict(int)
        i = 0
        count = 0
        for j in range(len(nums)):
            if freq[nums[j]] == 0:
                k -= 1
            freq[nums[j]] += 1

            while k < 0:
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    k += 1
                i += 1

            count += j - i + 1
        return count