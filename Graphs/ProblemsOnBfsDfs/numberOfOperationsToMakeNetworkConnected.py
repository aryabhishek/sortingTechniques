from disjointSet import DisjointSet
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        extra_edges = 0
        for u, v in connections:
            # check if u and v are already connected
            if ds.find_ultimate_parent(u) == ds.find_ultimate_parent(v):
                extra_edges += 1
            else:
                ds.union_by_rank(u, v)

        connected_components = 0

        for i in range(n):
            if ds.parent[i] == i:
                connected_components += 1

        ans = (
            connected_components - 1
        )  # we need at least n-1 edges to connect n nodes or provinces

        return ans if extra_edges >= ans else -1
