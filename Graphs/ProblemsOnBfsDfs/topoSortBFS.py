from collections import deque


class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indeg = [0 for i in range(V)]
        ans = []

        for i in range(V):
            for node in adj[i]:
                indeg[node] += 1

        q = deque()

        for i in range(V):
            if indeg[i] == 0:
                q.append(i)

        while q:
            node = q[0]
            ans.append(q.popleft())
            for adj_node in adj[node]:
                indeg[adj_node] -= 1
                if indeg[adj_node] == 0:
                    q.append(adj_node)

        return ans
