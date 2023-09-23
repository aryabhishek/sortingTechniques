class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        self.vis = [0]*(n)
        adj_ls = [[] for _ in range(n)]
        count = 0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj_ls[i].append(j)
                    adj_ls[j].append(i)

        for i in range(n):
            if self.vis[i] == 0:
                self.dfs(i, adj_ls)
                count += 1

        return count

    def dfs(self, node, adj):
        self.vis[node] = 1

        for it in adj[node]:
            if self.vis[it] == 0:
                self.dfs(it, adj)
