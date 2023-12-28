"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Link: https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n

        while True:
            slow = self.digit_sum_square(slow)
            fast = self.digit_sum_square(fast)
            fast = self.digit_sum_square(fast)

            if slow == fast:
                break

        if slow == 1:
            return True

        return False

    def digit_sum_square(self, n: int) -> int:
        total, temp = 0, 0

        while n:
            temp = n % 10
            total += temp * temp
            n //= 10

        return total
