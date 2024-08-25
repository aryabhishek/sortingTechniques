"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

https://leetcode.com/problems/subarray-sum-equals-k/
"""

def brute_force(nums, k): # TC: O(n^3), SC: O(1)

    def gen_subarrays(arr):
        n = len(arr)
        ans = []
        for i in range(n):
            for j in range(i, n):
                temp = []
                for k in range(i, j+1):
                    temp.append(arr[k])

                ans.append(temp)

        return ans

    subarrays = gen_subarrays(nums)
    ans = 0
    for sub in subarrays:
        if sum(sub) == k:
            ans += 1

    return ans


def optimal(nums, k): # TC: O(n), SC: O(n)
    res = 0
    cur_sum = 0
    pre_sum = {0: 1}

    for n in nums:
        cur_sum += n
        diff = cur_sum - k
        res += pre_sum.get(diff, 0)
        pre_sum[cur_sum] = pre_sum.get(cur_sum, 0) + 1

    return res


if __name__ == "__main__":
    arr = [3, -3, 1, 1, 1]
    print(optimal(arr, 3))
