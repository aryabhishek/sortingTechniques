import heapq


class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.

    def dijkstra(self, V, adj, S):
        # code here

        dist = [float("inf") if i != S else 0 for i in range(V)]

        pq = [(0, S)]

        while pq:
            # dis is the distrance from src to cur node
            dis, node = heapq.heappop(pq)

            for adj_node, wt in adj[node]:
                # wt is the distance from cur node to adj node
                new_dis = dis + wt

                if new_dis < dist[adj_node]:
                    dist[adj_node] = new_dis
                    heapq.heappush(pq, (new_dis, adj_node))

        return dist
