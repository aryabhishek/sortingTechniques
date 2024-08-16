"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

https://leetcode.com/problems/all-paths-from-source-to-target/
"""

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []

        def dfs(node, adj, temp):
            temp.append(node)
            if node == n - 1:
                paths.append(temp.copy())

            for it in adj[node]:
                dfs(it, adj, temp)
            temp.pop()

        dfs(0, graph, [])
        return paths
