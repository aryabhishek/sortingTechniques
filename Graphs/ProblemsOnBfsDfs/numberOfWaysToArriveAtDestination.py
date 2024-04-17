from typing import List
import heapq, sys


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        adj = [[] for i in range(n)]

        for u, v, time in roads:
            adj[u].append([v, time])
            adj[v].append([u, time])

        ways = [0 for i in range(n)]
        ways[0] = 1

        dist = [sys.maxsize for i in range(n)]
        dist[0] = 0

        q = [[0, 0]]  # [dis, node]

        while q:
            dis, node = q[0]
            heapq.heappop(q)
            # adjNode, weight
            for v, time in adj[node]:
                if dis + time < dist[v]:
                    dist[v] = dis + time
                    heapq.heappush(q, [dis + time, v])
                    ways[v] = ways[node]  # coz visiting first time
                elif dis + time == dist[v]:
                    ways[v] = (ways[v] + ways[node]) % mod

        return ways[n - 1] % mod  # n-1 is the destination
