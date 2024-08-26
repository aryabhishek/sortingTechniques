"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

https://leetcode.com/problems/move-zeroes/
"""

def move_zeros_to_end(nums):
    p = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[p],nums[i] = nums[i],nums[p]
            p += 1


if __name__ == "__main__":
    arr = [1,2,3,0,0,0,4,0,0,5,0,6,0,7]
    move_zeros_to_end(arr)
    print(arr)
