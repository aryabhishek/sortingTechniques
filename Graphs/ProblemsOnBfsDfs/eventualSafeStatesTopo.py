"""

"""

from typing import List
from collections import deque


class Solution:
    def eventualSafeNodes(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        adj_rev = [[] for i in range(V)]
        indeg = [0 for i in range(V)]
        safe_nodes = []

        for i in range(V):
            for adj_node in adj[i]:
                adj_rev[adj_node].append(i)
                indeg[i] += 1

        q = deque()

        for i in range(V):
            if indeg[i] == 0:
                q.append(i)

        while q:
            node = q[0]
            safe_nodes.append(q.popleft())

            for adj_node in adj_rev[node]:
                indeg[adj_node] -= 1
                if indeg[adj_node] == 0:
                    q.append(adj_node)

        safe_nodes.sort()
        return safe_nodes
