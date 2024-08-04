"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105

https://leetcode.com/problems/equal-row-and-column-pairs
"""

from collections import defaultdict


class Solution:  # Brute Force
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        count = 0

        for row in range(n):
            for col in range(n):
                is_equal = True
                for i in range(n):
                    if grid[row][i] != grid[i][col]:
                        is_equal = False
                        break
                if is_equal:
                    count += 1
        return count


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        row_map = defaultdict(int)
        count = 0

        for row in grid:
            row_map[tuple(row)] += 1

        for r in range(n):
            col = tuple()
            for c in range(n):
                col += (grid[c][r],)
            count += row_map[col]

        return count
