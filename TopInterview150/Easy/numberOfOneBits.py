"""
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
Link: https://leetcode.com/problems/number-of-1-bits/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        def count_set_bits(s: str, idx: int, count: int) -> int:
            if idx == len(s):
                return count

            if s[idx] == "1":
                count += 1

            return count_set_bits(s, idx + 1, count)

        return count_set_bits(bin(n), 0, 0)
