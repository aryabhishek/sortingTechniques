class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        def max_non_overlapping(arr):
            arr.sort(key=lambda tup: tup[1])
            limit = arr[0][1]  # end time
            count = 1

            for i in range(1, len(arr)):
                if arr[i][0] >= limit:
                    limit = arr[i][1]
                    count += 1
            return count

        return len(intervals) - max_non_overlapping(intervals)
