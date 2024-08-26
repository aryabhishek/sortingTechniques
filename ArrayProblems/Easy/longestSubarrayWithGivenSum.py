"""
Given an array arr containing n integers and an integer k. Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k
"""

def solution(a, k):
    left, right = 0, 0
    n = len(a)

    total = a[0]
    ans = 0

    while right < n:

        while left <= right and total > k:
            total -= a[left]
            left += 1

        if total == k:
            ans = max(ans, right - left + 1)

        right += 1
        if right < n:
            total += a[right]

    return ans


if __name__ == "__main__":
    arr = [1,2,3,3,4,6,6,7,5,1,1,1,1,1,4]
    k = 12

    print(solution(arr, k))
