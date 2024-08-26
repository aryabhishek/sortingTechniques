"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

https://leetcode.com/problems/longest-consecutive-sequence/
"""

def brute_force(arr):
    n = len(arr)

    ans = 1

    for i in range(n):
        start = arr[i]
        count = 1
        while start + 1 in arr:
            start += 1
            count += 1

        ans = max(count, ans)

    return ans


def better(arr):
    sorted_array = sorted(arr)
    n = len(arr)
    ans = 0
    last_min = float("-inf")
    count = 0

    for i in range(n):
        x = sorted_array[i]

        if x - 1 == last_min:
            count += 1
            last_min = x
        
        elif x != last_min:
            count = 1
            last_min = x

        ans = max(ans, count)

    return ans


def optimal(arr):
    n = len(arr)
    if n == 0:
        return 0

    a_set = set(arr)

    ans = 1

    for it in a_set:

        if it - 1 not in a_set:
            x = it + 1
            count = 1

            while x in a_set:
                x += 1
                count += 1

            ans = max(ans, count)

    return ans


if __name__ == "__main__":
    arr = [5,8,3,2,1,4]
    print(brute_force(arr))
    print(better(arr))
    print(optimal(arr))

    
