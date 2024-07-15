"""
Given an integer n, return the number of prime numbers that are strictly less than n.
"""

from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        prime = [1] * n
        prime[0] = prime[1] = 0
        root = int(sqrt(n))
        count = n - 2  # removing 1 and 0

        for i in range(2, root + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    if prime[j]:
                        count -= 1
                        prime[j] = 0
        return count
