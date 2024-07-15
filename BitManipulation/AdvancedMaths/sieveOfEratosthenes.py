"""
Print all prime numbers from 1 to N efficiently.
"""

from math import sqrt


class Solution:
    def print_primes(self, N):
        # Code here
        if N == 1:
            return [2]

        prime = [True for i in range(N + 1)]

        for i in range(2, int(sqrt(N)) + 1):
            if prime[i]:
                for j in range(i * i, N + 1, i): # iterate over all the multiples of i till N
                    prime[j] = False

        for i in range(2, N + 1):
            if prime[i]:
                print(i, end=" ")


if __name__ == "__main__":
    N = 0
    sol = Solution()
    sol.print_primes(N)
