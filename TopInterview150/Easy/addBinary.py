"""
Given two binary strings a and b, return their sum as a binary string.
Link: https://leetcode.com/problems/add-binary/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = ""
        carry = "0"

        for i in range(max_len - 1, -1, -1):
            carry, total = self.full_adder(int(a[i]), int(b[i]), int(carry))
            result = total + result

        if carry == "1":
            result = carry + result

        return result

    def full_adder(self, a, b, c):
        total = a ^ b ^ c
        carry = a & b | b & c | a & c

        return str(carry), str(total)
