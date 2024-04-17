class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    """
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    """

    def bellman_ford(self, V, edges, S):
        # code here
        maxx = 10**8

        dist = [maxx for i in range(V)]
        dist[S] = 0

        for i in range(V - 1): # relax edges V-1 times
            for u, v, wt in edges:
                if dist[u] != maxx and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        for u, v, wt in edges:
            if dist[u] != maxx and dist[u] + wt < dist[v]: # detect negative cycle
                return [-1]

        return dist
