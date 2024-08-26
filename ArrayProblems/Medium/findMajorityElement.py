"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

https://leetcode.com/problems/majority-element/
"""

def brute_force(arr): # TC: O(n*log(n)), SC: O(1)
    arr.sort()
    mid = arr[len(arr)//2]
    return mid


def better(arr): #TC: O(2n), SC: O(n)
    n = len(arr)

    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for key, value in freq.items():
        if value > n//2:
            return key
        

# Moore's Voting Algorithm
def optimal(arr): # TC: O(n), SC: O(1)
    vote = 1
    major = arr[0]
    for i in range(1, len(arr)):

        if arr[i] == major:
            vote += 1
        else:
            vote -= 1

        if vote == 0:
            major = arr[i]  
            vote = 1 
        
    return major


if __name__ == "__main__":
    arr = [2,2,1,1,1,2,2]
    print("Brute Force: ",brute_force(arr))
    print("Better Solution: ",better(arr))
    print("Optimal: ", optimal(arr))
