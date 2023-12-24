"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Link: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        vote = 1
        major = nums[0]
        for i in range(1, len(nums)):
             
            if nums[i] == major:
                vote += 1
            else:
                vote -= 1

            if vote == 0:
                major = nums[i]  
                vote = 1 
            
        return major
        