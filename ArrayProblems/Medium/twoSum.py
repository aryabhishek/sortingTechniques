"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

https://leetcode.com/problems/two-sum/
"""

def twoSum(nums: list[int], target: int) -> list[int]:
        
        seen = {}

        for i, val in enumerate(nums):

            rem = target - val

            if rem in seen:
                return [i, seen[rem]]

            seen[val] = i


if __name__ == "__main__":
    arr = [2,7,11,15]
    target = 9

    print(twoSum(arr, target))
