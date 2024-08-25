"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

https://leetcode.com/problems/sort-colors/
"""

def my_solution(nums): # better than sorting, TC: O(2n), SC: O(1)
    zero = 0
    one = 0
    two = 0

    for num in nums:
        if num == 0:
            zero += 1
        
        elif num == 1:
            one += 1

        else:
            two += 1

    ind = 0
    for i in range(zero):
        nums[ind] = 0
        ind += 1

    for i in range(one):
        nums[ind] = 1
        ind += 1

    for i in range(two):
        nums[ind] = 2
        ind += 1


# Dutch National Flag Algorithm

def optimal(arr): # TC: O(n), SC:O(1)
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        
        elif arr[mid] == 1:
            mid += 1

        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    

if __name__ == "__main__":
    arr = [2,0,2,1,1,0]
    optimal(arr)
    print(arr)
