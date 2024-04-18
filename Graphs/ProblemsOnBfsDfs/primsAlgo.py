from heapq import heappush, heappop


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    """MST means a graph with V-1 edges with minimised weight"""

    def spanningTree(self, V, adj):
        # code here
        vis = [0 for i in range(V)]

        pq = [[0, 0]]  # weight, node
        ans = 0

        while pq:
            wt, node = heappop(pq)

            if vis[node]:
                continue
            vis[node] = 1
            ans += wt

            for v, w in adj[node]:
                if not vis[v]:
                    heappush(pq, [w, v])
        return ans
