"""
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
"""

from bisect import bisect_left
from typing import List
from math import ceil


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        res = []

        for spell in spells:
            min_potion = ceil(success / spell)
            index = bisect_left(potions, min_potion)
            count = len(potions) - index
            res.append(count)

        return res
