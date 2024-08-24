"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

https://leetcode.com/problems/critical-connections-in-a-network/
"""

from typing import List


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        self.adj = [[] for _ in range(n)]
        self.bridges = []
        self.vis = [0] * n
        self.timer = 1
        self.tin = [0] * n
        self.low = [0] * n

        for u, v in connections:
            self.adj[u].append(v)
            self.adj[v].append(u)

        for i in range(n):
            if self.vis[i] == 0:
                self.dfs(i, -1)

        return self.bridges

    def dfs(self, node, parent):
        self.vis[node] = 1
        self.tin[node] = self.low[node] = self.timer
        self.timer += 1

        for it in self.adj[node]:
            if it == parent:
                continue

            if self.vis[it] == 0:
                self.dfs(it, node)
                self.low[node] = min(self.low[node], self.low[it])

                if self.low[it] > self.tin[node]:
                    self.bridges.append([node, it])
            else:
                self.low[node] = min(self.low[node], self.tin[it])
