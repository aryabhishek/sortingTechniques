class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        res, i = [], 0
        n = len(intervals)

        while i < n:
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                i += 1

            elif intervals[i][0] <= newInterval[1]:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                i += 1
            else:
                break

        res.append(newInterval)
        res.extend(intervals[i:])

        return res
