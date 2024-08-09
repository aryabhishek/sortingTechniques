"""
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

https://leetcode.com/problems/total-cost-to-hire-k-workers/
"""

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = []
        right = []
        heapify(left)
        heapify(right)
        n = len(costs)
        l = 0
        r = n - 1
        cost = 0

        for i in range(k):

            while l <= r and len(left) < candidates:
                heappush(left, costs[l])
                l += 1

            while l <= r and len(right) < candidates:
                heappush(right, costs[r])
                r -= 1

            left_min = left[0] if left else float("inf")
            right_min = right[0] if right else float("inf")

            if left_min <= right_min:
                cost += heappop(left)
            else:
                cost += heappop(right)

        return cost


if __name__ == "__main__":
    costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k = 3
    candidates = 4

    print(Solution().totalCost(costs, k, candidates))
