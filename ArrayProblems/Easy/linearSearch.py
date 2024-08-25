"""
Given an array arr[] sorted in ascending order of size N and an integer K. Check if K is present in the array or not.

https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=who-will-win
"""

def linear_search(arr, num):
    n = len(arr)

    for i in range(n):
        if arr[i] == num:
            return i
    return -1


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    print(linear_search(arr, 4))
