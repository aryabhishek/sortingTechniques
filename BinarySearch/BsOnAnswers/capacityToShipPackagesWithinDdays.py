"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
"""


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def days_to_load(weights, cap):
            d, temp, i = 0, cap, 0

            while i < len(weights):
                if weights[i] > temp:
                    d += 1
                    temp = cap
                else:
                    temp -= weights[i]
                    i += 1

            return d + 1 if temp < cap else d

        n = len(weights)

        left = max(weights)
        right = sum(weights)

        while left <= right:
            cap = (left + right) // 2
            days_with_cap = days_to_load(weights, cap)

            if days_with_cap <= days:
                right = cap - 1
            else:
                left = cap + 1

        return left
