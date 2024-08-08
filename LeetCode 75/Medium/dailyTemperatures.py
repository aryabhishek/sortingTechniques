"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

https://leetcode.com/problems/daily-temperatures
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        ans = [0]
        stk = [len(temperatures) - 1]

        for i in range(len(temperatures) - 2, -1, -1):
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()

            if not stk:
                ans.append(0)

            else:
                ans.append(stk[-1] - i)

            stk.append(i)

        return ans[::-1]
