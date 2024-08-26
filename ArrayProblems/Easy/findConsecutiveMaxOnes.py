"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

https://leetcode.com/problems/max-consecutive-ones/
"""

def max_consecutive_ones(arr):
    maxi = 0
    count = 0

    for num in arr:
        if num == 1:
            count += 1
            maxi = max(count, maxi)

        else:
            count = 0

    return maxi


if __name__ == "__main__":
    arr = [1,1,0,1,1,1,0,0,1,1,0]
    print(max_consecutive_ones(arr))
