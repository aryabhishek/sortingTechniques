"""
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

https://leetcode.com/problems/maximal-network-rank/
"""

from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(n)]
        rank = [0] * n

        for u, v in roads:
            grid[u][v] = 1
            grid[v][u] = 1
            rank[u] += 1
            rank[v] += 1

        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                total = rank[i] + rank[j]
                if grid[i][j] == 1:
                    total -= 1
                max_rank = max(max_rank, total)

        return max_rank
