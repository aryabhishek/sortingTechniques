"""
Given an array, arr. The task is to find the largest element in it.

https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array
"""

def find_max(arr):
    n = len(arr)

    largest = arr[0]

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    return largest

if __name__ == "__main__":
    arr = [1,2,3,4,5]

    largest_element = find_max(arr) # finding max

    print(largest_element)
