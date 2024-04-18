from disjointSet import DisjointSet


class Solution:
    def numProvinces(self, adj, V):
        count = 0
        ds = DisjointSet(V)

        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                    ds.union_by_size(i, j)

        for i in range(V):
            if ds.find_ultimate_parent(i) == i:
                count += 1

        return count
