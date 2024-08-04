"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length

https://leetcode.com/problems/max-consecutive-ones-iii/
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        l = r = 0
        zeros = ans = 0

        while r < n:
            if nums[r] == 0:
                zeros += 1

            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            if zeros <= k:
                ans = max(ans, r - l + 1)

            r += 1

        return ans
