"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Link: https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def plusOne(self, digits: int) -> int:
        n = len(digits)

        # if the last digit is 9
        if digits[-1] == 9:
            i = n - 1  # change all connected nines to zeroes
            while i >= 0 and digits[i] == 9:
                digits[i] = 0
                i -= 1

            # if all the digits are 9
            if i == -1:
                digits.insert(0, 1)
            else:  # rightmost non-nine digit gets the carry 1
                digits[i] += 1
        else:
            digits[-1] += 1

        return digits
