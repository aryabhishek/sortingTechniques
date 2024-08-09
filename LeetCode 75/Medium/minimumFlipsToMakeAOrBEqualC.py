"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a or b or c:
            if c & 1 == 1:
                if a & 1 == 0 and b & 1 == 0:
                    flips += 1

            else:
                if a & 1 == 1:
                    flips += 1
                if b & 1 == 1:
                    flips += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flips


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return ((a | b) ^ c).bit_count() + ((a & b) & ((a & b) ^ c)).bit_count()
