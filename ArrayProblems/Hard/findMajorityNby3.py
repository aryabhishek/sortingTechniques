"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

https://leetcode.com/problems/majority-element-ii/
"""

def solution(arr):
    n = len(arr)

    vote1 = 0
    vote2 = 0
    major1 = float("-inf")
    major2 = float("-inf")
    for i in range(n):

        if vote1 == 0 and major2 != arr[i]:
            vote1 = 1
            major1 = arr[i]

        elif vote2 == 0 and major1 != arr[i]:
            vote2 = 1
            major2 = arr[i]

        elif arr[i] == major1:
            vote1 += 1

        elif arr[i] == major2:
            vote2 += 1

        else:
            vote1 -= 1
            vote2 -= 1

    ls = []

    vote1, vote2 = 0, 0
    for i in range(n):
        if arr[i] == major1:
            vote1 += 1
        if arr[i] == major2:
            vote2 += 1

    mini = int(n / 3) + 1
    if vote1 >= mini:
        ls.append(major1)
    if vote2 >= mini:
        ls.append(major2)

    return ls


def leetcode_best(nums):
    if not nums:
        return []

    counter1, counter2 = 0, 0
    candidate1, candiate2 = None, None

    # 1st pas
    for n in nums:

        if candidate1 == n:
            counter1 += 1

        elif candiate2 == n:
            counter2 += 1

        elif counter1 == 0:
            candidate1 = n
            counter1 += 1

        elif counter2 == 0:
            candiate2 = n
            counter2 += 1

        else:
            counter1 -= 1
            counter2 -= 1

    # 2nd pass
    results = []
    for x in [candidate1, candiate2]:
        if nums.count(x) > len(nums) // 3:
            results.append(x)

    return results


if __name__ == "__main__":
    arr = [2, 2, 1, 3]
    print(solution(arr))
    print(leetcode_best(arr))
