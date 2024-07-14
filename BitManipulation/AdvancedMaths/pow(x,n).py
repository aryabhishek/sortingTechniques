"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1

        if n < 0:
            x = 1 / x
            n = -(n + 1)
            ans *= x

        while n > 0:
            if n % 2 == 1:  # odd
                n -= 1
                ans *= x
            else:  # even
                n //= 2
                x *= x

        return ans
