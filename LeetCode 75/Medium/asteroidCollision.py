"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

https://leetcode.com/problems/asteroid-collision/
"""


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stk = []

        for roid in asteroids:
            while stk and roid < 0 < stk[-1]:
                total = roid + stk[-1]
                if total < 0:
                    stk.pop()
                elif total > 0:
                    break
                else:
                    stk.pop()
                    break
            else:
                stk.append(roid)

        return stk
