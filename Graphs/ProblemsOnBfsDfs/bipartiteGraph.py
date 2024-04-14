from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]

        for i in range(len(color)): # graph can have diff components
            if color[i] == -1:
                if not self.bfs(i, graph, color):
                    return False

        return True
    
    def bfs(self, node, col, adj, color):
        color[node] = col

        for adj_node in adj[node]:
            if  color[adj_node] == -1:
                if not self.bfs(adj_node, 1-col, adj, color):
                    return False
            elif color[adj_node] == col:
                return False
            
        return True

    def bfs(self, start, adj, color):
        q = deque([start])
        color[start] = 0

        while q:
            node = q.popleft()

            for adj_node in adj[node]:
                if color[adj_node] == -1:
                    color[adj_node] = not color[node]
                    q.append(adj_node)
                elif color[adj_node] == color[node]:
                    return False

        return True
