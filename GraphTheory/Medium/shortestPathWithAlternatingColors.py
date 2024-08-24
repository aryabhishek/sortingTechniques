"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

https://leetcode.com/problems/shortest-path-with-alternating-colors
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        red, blue = defaultdict(list), defaultdict(list)

        for u, v in redEdges:
            red[u].append(v)

        for u, v in blueEdges:
            blue[u].append(v)

        q = deque()  # [node, length, edgeColor]
        q.append((0, 0, None))
        vis = set()
        ans = [-1] * n

        while q:
            node, length, edgeColor = q.popleft()
            if ans[node] == -1:
                ans[node] = length

            if edgeColor != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in vis:
                        q.append((nei, length + 1, "RED"))
                        vis.add((nei, "RED"))

            if edgeColor != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in vis:
                        q.append((nei, length + 1, "BLUE"))
                        vis.add((nei, "BLUE"))

        return ans
