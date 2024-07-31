"""
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

https://leetcode.com/problems/filling-bookcase-shelves/
"""
from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        self.width = shelfWidth
        self.dp = [[-1] * 1001 for _ in range(1002)]
        return self.solve(0, books, 0, self.width)

    def solve(self, idx, books, height, width):
        if idx >= len(books):
            return height
        if self.dp[idx][width] != -1:
            return self.dp[idx][width]

        book_width, book_height = books[idx]
        keep = float('inf')
        if book_width <= width:
            keep = self.solve(idx + 1, books, max(book_height, height), width - book_width)
        skip = height + self.solve(idx + 1, books, book_height, self.width - book_width)

        self.dp[idx][width] = min(keep, skip)
        return self.dp[idx][width]