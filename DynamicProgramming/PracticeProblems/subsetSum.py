"""
Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 
Link: https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638
"""


class MySolution:
    def isSubsetSum(self, arr, sum):
        # code here
        self.memo = {}
        return self.solve(0, arr, sum)

    def solve(self, i, arr, target):
        if i >= len(arr) and target != 0:
            return False

        if target == 0:
            return True

        if (i, target) in self.memo:
            return self.memo[(i, target)]

        if arr[i] <= target:
            self.memo[(i, target)] = self.solve(
                i + 1, arr, target - arr[i]
            ) or self.solve(i + 1, arr, target)
            return self.memo[(i, target)]

        self.memo[(i, target)] = self.solve(i + 1, arr, target)
        return self.memo[(i, target)]


class TopDownApproach:
    def isSubsetSum(self, arr, sum):
        memo = [[-1]*(sum+1) for i in range(len(arr) + 1)]
        for i in range(len(arr)+1):
            for j in range(sum + 1):
                if i == 0:
                    memo[i][j] = 0
                if j == 0:
                    memo[i][j] = 1

        for i in range(1, len(arr)+1): # index of elements in arr
            for j in range(1, sum+1): # sum to achieve
                if arr[i-1] <= j:
                    memo[i][j] =  memo[i-1][j-arr[i-1]] or memo[i-1][j]
                else:
                    memo[i][j] = memo[i-1][j]

        return memo[len(arr)][sum]