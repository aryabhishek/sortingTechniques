"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

https://leetcode.com/problems/rearrange-array-elements-by-sign
"""

def brute_force(nums):  # If negatives != positives
    pos = []
    neg = []
    
    for i in range(len(nums)):
        if nums[i] > 0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    
    if len(pos) < len(neg):
        for i in range(len(pos)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        
        index = len(pos)*2
        for i in range(len(neg)-len(pos)):
            nums[index] = neg[len(pos)+i]
            index += 1
    
    else:
        for i in range(len(neg)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        
        index = len(neg)*2
        for i in range(len(pos)-len(neg)):
            nums[index] = pos[len(neg)+i]
            index += 1
    
    return nums


def optimal(nums):  # if negatives == positives
    pos = 0
    neg = 1
    ans = [0]*len(nums)

    for num in nums:
        if num < 0:
            ans[neg] = num
            neg += 2
        else:
            ans[pos] = num
            pos += 2

    return ans


if __name__ == "__main__":
    inputs = [
        [3, 1, -2, -5, 2, -4],
        [1, 2, -3, -1, -2, 3],
        [-2, -3, 4, 5, 6,7],
        [-1, -2, -3, 1, 2, -6, -4, -8, 4, 5]
    ]

    for inp in inputs:
        print(brute_force(inp))
    print()
    print(optimal(inputs[0]))
    print(optimal(inputs[1]))

