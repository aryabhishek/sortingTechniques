"""
Comple the function findPrimeFactors(), which takes a positive number N as input and returns a vector consisting of prime factors. You should implement Sieve algorithm to solve this problem.
"""

from math import sqrt


class Solution:
    def sieve(self):
        N = 2 * (10**5)
        self.prime = [i for i in range(N + 1)]
        root = int(sqrt(N))
        for i in range(2, root + 1):
            if self.prime[i] == i:
                for j in range(i * i, N + 1, i):
                    if self.prime[j] == j:
                        self.prime[j] = i

    def findPrimeFactors(self, N):
        # Code here
        ans = []
        while N > 1:
            ans.append(self.prime[N])
            N //= self.prime[N]

        return ans
