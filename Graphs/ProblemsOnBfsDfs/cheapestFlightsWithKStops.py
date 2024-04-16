import sys
from collections import deque


class Solution:
    def CheapestFLight(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]

        for u, v, wt in flights:
            adj[u].append([v, wt])

        dist = [sys.maxsize for _ in range(n)]
        dist[src] = 0
        q = deque()
        q.append([0, src, 0])  # [stops, node, cost]

        while q:
            stops, node, cost = q.popleft()

            if stops > k:
                continue

            for v, wt in adj[node]:
                if cost + wt < dist[v]:
                    dist[v] = cost + wt
                    q.append([stops + 1, v, cost + wt])

        if dist[dst] == sys.maxsize:
            return -1

        return dist[dst]
