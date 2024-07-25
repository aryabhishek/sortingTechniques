"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
"""

from math import atan2, degrees
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n == 1:
            return 1
        res = 0
        for i in range(n):
            dic = {}
            for j in range(n):
                if i == j:
                    continue
                dy = points[j][1] - points[i][1]
                dx = points[j][0] - points[i][0]
                theeta = degrees(atan2(dy, dx))
                if theeta not in dic:
                    dic[theeta] = 1
                else:
                    dic[theeta] += 1
            res = max(res, max(dic.values()) + 1)

        return res
