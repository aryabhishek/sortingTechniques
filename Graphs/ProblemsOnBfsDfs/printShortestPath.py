from typing import List
import heapq


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # code here
        dist = [float("inf")] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        parent = [i for i in range(n + 1)]

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))  # undirected

        pq = [(0, 1)]  # 1 is the source
        dist[1] = 0

        while pq:
            dis, node = heapq.heappop(pq)

            for adj_node, wt in adj[node]:
                new_dis = dis + wt

                if new_dis < dist[adj_node]:
                    dist[adj_node] = new_dis
                    parent[adj_node] = node
                    heapq.heappush(pq, (new_dis, adj_node))

        if dist[n] == float("inf"):
            return [-1]

        # reconstructing the path
        path = []
        node = n
        while parent[node] != node:
            path.append(node)
            node = parent[node]

        path.append(1)
        path.append(dist[n])
        path.reverse()

        return path
