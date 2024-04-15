from collections import deque


class Solution:

    def bfs(self, node, adj, dist):
        q = deque([node])

        while q:
            v = q.popleft()

            for adj_node in adj[v]:
                if dist[v] + 1 < dist[adj_node]:
                    dist[adj_node] = dist[v] + 1
                    q.append(adj_node)

    def shortestPath(self, edges, n, m, src):
        # code here
        dist = [float("inf") if i != src else 0 for i in range(n)]

        adj = [[] for i in range(n)]

        for i in range(m):
            u = edges[i][0]
            v = edges[i][1]
            adj[u].append(v)
            adj[v].append(u)  # undirected

        self.bfs(src, adj, dist)

        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist
