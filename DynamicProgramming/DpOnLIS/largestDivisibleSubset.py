class Solution:
    def largestDivisibleSubset(self, arr: list[int]) -> list[int]:
        n = len(arr)
        arr.sort()

        dp = [1] * n
        hash_arr = list(range(n))

        for i in range(n):
            for prev in range(i):
                if arr[i] % arr[prev] == 0 and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    hash_arr[i] = prev

        ans = -1
        last_index = -1

        for i in range(n):
            if dp[i] > ans:
                ans = dp[i]
                last_index = i

        result = [arr[last_index]]

        while hash_arr[last_index] != last_index:
            last_index = hash_arr[last_index]
            result.append(arr[last_index])

        return result


