"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

https://leetcode.com/problems/non-overlapping-intervals/
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        def max_non_overlapping(arr):
            arr.sort(key=lambda tup: tup[1])
            limit = arr[0][1]
            count = 1

            for i in range(1, len(arr)):
                if arr[i][0] >= limit:
                    limit = arr[i][1]
                    count += 1
            return count

        return len(intervals) - max_non_overlapping(intervals)
