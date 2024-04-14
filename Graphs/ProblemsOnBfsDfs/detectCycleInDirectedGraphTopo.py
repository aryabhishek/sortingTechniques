from collections import deque


class Solution:

    def isCyclic(self, V, adj):
        indeg = [0 for i in range(V)]

        for i in range(V):
            for node in adj[i]:
                indeg[node] += 1

        q = deque()
        count = 0

        for i in range(V):
            if indeg[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            count += 1
            for adj_node in adj[node]:
                indeg[adj_node] -= 1
                if indeg[adj_node] == 0:
                    q.append(adj_node)

        return count != V
