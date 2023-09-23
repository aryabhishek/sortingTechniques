class Solution:

    def dfsOfGraph(self, V, adj):
        # code here
        self.vis = [0]*V
        start = 0

        self.ans = []
        self.dfs(start, adj)
        return self.ans

    def dfs(self, node, adj):
        self.vis[node] = 1
        self.ans.append(node)

        for it in adj[node]:
            if self.vis[it] == 0:
                self.dfs(it, adj)
