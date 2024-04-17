import sys
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[sys.maxsize]*n for i in range(n)]

        for u, v, wt in edges:
            dist[u][v] = wt
            dist[v][u] = wt # undirected graph

        for i in range(n):
            dist[i][i] = 0

        self.shortest_distance(dist)

        min_count = n
        ans = -1

        for city in range(n):
            count = 0
            for adj_city in range(len(dist[0])):
                if dist[city][adj_city] <= distanceThreshold:
                    count += 1
            if count <= min_count:
                min_count = count
                ans = city

        return ans

    def shortest_distance(self, matrix):
        n = len(matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])