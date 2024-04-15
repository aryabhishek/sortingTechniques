from typing import List
from collections import deque


class Solution:

    def topoSort(self, node, adj, vis, stack):
        vis[node] = 1

        for adj_node in adj[node]:
            v = adj_node[0]
            if not vis[v]:
                self.topoSort(v, adj, vis, stack)

        stack.append(node)

    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        vis = [0 for i in range(n)]
        # [[(0, 1)]]

        for i in range(m):
            u = edges[i][0]
            v = edges[i][1]
            wt = edges[i][2]
            adj[u].append((v, wt))

        stack = deque()

        for i in range(
            n
        ):  # to cover all the components (if the graph has multiple connected components)
            if not vis[i]:
                self.topoSort(i, adj, vis, stack)

        dist = [float("inf") for i in range(n)]
        dist[0] = 0  # assume source to be 0

        while stack:
            node = stack.pop()

            for adj_node in adj[node]:
                v, wt = adj_node

                if dist[node] + wt < dist[v]:
                    dist[v] = dist[node] + wt

        for i in range(len(dist)):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist
