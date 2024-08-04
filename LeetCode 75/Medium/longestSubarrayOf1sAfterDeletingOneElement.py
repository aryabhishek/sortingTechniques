"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:  # my solution
        zeros = 0
        n = len(nums)
        ans = l = 0

        for r in range(n):
            if nums[r] == 0:
                zeros += 1

            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            ans = max(ans, r - l)

        return ans


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:  # Clean approach
        n = len(nums)
        ans = l = 0
        zero_idx = -1

        for r in range(n):
            if nums[r] == 0:
                l = zero_idx + 1
                zero_idx = r

            ans = max(ans, r - l)

        return ans
