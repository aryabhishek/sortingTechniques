from disjointSet import DisjointSet


class Solution:

    def spanningTree(self, V, adj):
        edges = []
        ans = 0

        for i in range(V):
            for v, wt in adj[i]:
                edges.append([wt, i, v])

        ds = DisjointSet(V)
        edges.sort() # because we need to be greedy

        for wt, u, v in edges:
            if ds.find_ultimate_parent(u) != ds.find_ultimate_parent(v):
                ans += wt
                ds.union_by_size(u, v)

        return ans
