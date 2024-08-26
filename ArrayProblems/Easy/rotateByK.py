"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

https://leetcode.com/problems/rotate-array/
"""

def rotate_arr_by_k(arr, k): # TC: O(n+k), SC: O(k)
    n = len(arr)
    k = k % n

    temp = [arr[i] for i in range(k)]
    
    for i in range(k, n):
        arr[i-k] = arr[i]

    for i in range(n-k, n):
        arr[i] = temp[i-n+k]


def optimal_rotation(arr, k): # TC: O(2n), SC: O(1)

    def reverse(start, end):

        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    n = len(arr)
    k = k%n
    reverse(0, k-1) # reversing from start to k (zero indexed)
    reverse(k, n-1) # reversing from k + 1 to end (zero indexed)
    reverse(0, n-1) # reversing from start to end


def my_solution(arr, k): # TC: O(2n), SC: O(n)
    n = len(arr)
    temp = []

    for i in range(n):
        temp.append(arr[(i+k)%n])

    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    optimal_rotation(arr, 2)
    print(arr)

