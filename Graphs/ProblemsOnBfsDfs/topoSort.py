from collections import deque


class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        vis = [0 for i in range(V)]
        stack = deque()
        ans = []

        for i in range(V):
            if not vis[i]:
                self.dfs(i, adj, vis, stack)

        while stack:
            ans.append(stack.pop())

        return ans

    def dfs(self, node, adj, vis, stack):
        vis[node] = 1

        for adj_node in adj[node]:
            if not vis[adj_node]:
                self.dfs(adj_node, adj, vis, stack)

        stack.append(node)
