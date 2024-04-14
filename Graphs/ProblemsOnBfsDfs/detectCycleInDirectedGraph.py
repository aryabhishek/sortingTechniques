class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        vis = [0 for i in range(V)]
        
        for i in range(V):
            if not vis[i]:
                if self.dfs(i, adj, vis):
                    return True
                    
        return False
                
    def dfs(self, node, adj, vis):
        vis[node] = 2
        
        for adj_node in adj[node]:
            if not vis[adj_node]:
                if self.dfs(adj_node, adj, vis):
                    return True
            elif vis[adj_node] == 2:
                return True
        vis[node] = 1
                    
        return False
