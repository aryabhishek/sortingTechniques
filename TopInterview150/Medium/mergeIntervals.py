"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Link: https://leetcode.com/problems/merge-intervals
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda interval: interval[0])
        ans = []

        start, end = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                ans.append([start, end])
                start, end = interval

        ans.append([start, end])

        return ans
