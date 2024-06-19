"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""

from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def get_time(arr, eating_rate):
            req_time = 0

            for i in range(len(arr)):
                req_time += ceil(arr[i] / eating_rate)

            return req_time

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            time_req = get_time(piles, mid)

            if time_req <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left
