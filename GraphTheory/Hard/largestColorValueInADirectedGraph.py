"""
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
"""

from collections import deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = [[] for _ in range(n)]
        t = [[0] * 26 for _ in range(n)]
        indeg = [0] * n

        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1

        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
                t[i][ord(colors[i]) - 97] = 1

        ans = count = 0

        while q:
            node = q.popleft()
            count += 1
            ans = max(ans, max(t[node]))

            for adj_node in adj[node]:
                for i in range(26):
                    t[adj_node][i] = max(
                        t[adj_node][i],
                        t[node][i] + (1 if colors[adj_node] == chr(i + 97) else 0),
                    )
                indeg[adj_node] -= 1
                if indeg[adj_node] == 0:
                    q.append(adj_node)

        return ans if count == n else -1
