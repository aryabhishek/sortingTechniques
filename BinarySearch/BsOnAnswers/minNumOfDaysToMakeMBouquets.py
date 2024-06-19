"""
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
"""


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def is_possible(days, today, num_of_bukays, flowers_in_one_bukay):
            count = bukay = 0

            for day in days:
                if day <= today:
                    count += 1
                else:
                    bukay += count // flowers_in_one_bukay
                    count = 0
            bukay += count // flowers_in_one_bukay
            return bukay >= num_of_bukays

        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left <= right:
            mid_day = (left + right) // 2

            if is_possible(bloomDay, mid_day, m, k):
                right = mid_day - 1
            else:
                left = mid_day + 1

        return left
