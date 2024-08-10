"""
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
.

Return the minimum cuts needed for a palindrome partitioning of s.

https://leetcode.com/problems/palindrome-partitioning-ii
"""


class Solution:  # TLE
    def minCut(self, s: str) -> int:
        self.s = s
        self.n = len(s)
        self.dp = [-1] * self.n
        return self.solve(0) - 1

    def solve(self, i):
        if i == self.n:
            return 0
        if self.dp[i] != -1:
            return self.dp[i]

        min_cost = float("inf")

        for j in range(i, self.n):
            if self.is_palin(i, j):
                cost = 1 + self.solve(j + 1)
                min_cost = min(min_cost, cost)

        self.dp[i] = min_cost
        return min_cost

    def is_palin(self, i, j):
        while i < j:
            if self.s[i] != self.s[j]:
                return False
            i += 1
            j -= 1
        return True


class TabulationSolution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 0
        palin = [[False] * (n + 1) for i in range(n + 1)]
        
        for i in range(n):
            for j in range(i, n):
                palin[i][j] = self.is_palin(i, j, s)

        for i in range(n - 1, -1, -1):
            min_cost = float('inf')
            for j in range(i, n):
                if palin[i][j]:
                    cost = 1 + dp[j + 1]
                    min_cost = min(min_cost, cost)
            dp[i] = min_cost

        return dp[0] - 1
    
    def is_palin(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
if __name__ == "__main__":
    sol = TabulationSolution()
    s = "aab"
    print(sol.minCut(s))