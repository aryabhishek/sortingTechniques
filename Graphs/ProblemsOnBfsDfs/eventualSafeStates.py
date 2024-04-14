class Solution:
    def eventualSafeNodes(self, V: int, adj: list[list[int]]) -> list[int]:
        # code here
        vis = [0 for i in range(V)]
        ans = []

        for i in range(V):
            if not vis[i]:
                self.is_cyclic(i, adj, vis)

        for i in range(V):
            if vis[i] == 1:
                ans.append(i)

        return ans

    def is_cyclic(self, node, adj, vis):
        vis[node] = 2

        for adj_node in adj[node]:
            if not vis[adj_node]:
                if self.is_cyclic(adj_node, adj, vis):
                    return True
            elif vis[adj_node] == 2:
                return True
        vis[node] = 1  # only safe nodes will have visited marked as 1
        return False
