"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

https://leetcode.com/problems/smallest-number-in-infinite-set/
"""

from heapq import heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        self.added_back = []
        self.seen = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        if self.added_back:
            ele = heappop(self.added_back)
            self.seen.remove(ele)
            return ele
        else:
            self.smallest += 1
            return self.smallest - 1

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.seen:
            self.seen.add(num)
            heappush(self.added_back, num)
