"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

https://leetcode.com/problems/evaluate-division/
"""

from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}

        def add_edge(u, v, weight):
            if u not in graph:
                graph[u] = []
            graph[u].append((v, weight))

        def dfs(start, end, visited):
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph.get(start, []):
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1:
                        return result * weight
            return -1.0

        for (u, v), value in zip(equations, values):
            add_edge(u, v, value)
            add_edge(v, u, 1 / value)

        results = []
        for start, end in queries:
            if start not in graph or end not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(start, end, set()))

        return results
