"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""


class Solution:
    def candy(self, ratings: list[int]) -> int:  # 2 passes
        n = len(ratings)
        if n == 1:
            return n

        candy = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = max(candy[i], candy[i - 1] + 1)

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)


class Solution:
    def candy(self, ratings: list[int]) -> int:  # 1 pass
        candy = n = len(ratings)
        if n == 1:
            return candy

        i = 1
        while i < n:
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue

            # uphill
            peak = 0
            while ratings[i] > ratings[i - 1]:
                peak += 1
                candy += peak
                i += 1
                if i == n:
                    return candy

            # downhill
            dip = 0
            while i < n and ratings[i] < ratings[i - 1]:
                dip += 1
                candy += dip
                i += 1

            candy -= min(peak, dip)

        return candy
