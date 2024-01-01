"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Link: https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x == self.rev_sum(x)

    def rev_sum(self, n: int) -> int:
        rev = 0

        while n > 0:
            last = n % 10
            rev = rev * 10 + last
            n //= 10

        return rev
