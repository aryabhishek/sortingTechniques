"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
"""


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        l_sum = r_sum = 0
        n = len(cardPoints)

        for i in range(k):
            l_sum += cardPoints[i]

        max_sum = l_sum
        right = n - 1
        for i in range(k - 1, -1, -1):
            l_sum -= cardPoints[i]
            r_sum += cardPoints[right]
            right -= 1
            max_sum = max(max_sum, l_sum + r_sum)

        return max_sum
