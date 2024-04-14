"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def detectCycleTopo(V, adj):
            indeg = [0 for i in range(V)]

            for i in range(V):
                for node in adj[i]:
                    indeg[node] += 1

            q = deque()
            count = 0

            for i in range(V):
                if indeg[i] == 0:
                    q.append(i)

            while q:
                node = q.popleft()
                count += 1
                for adj_node in adj[node]:
                    indeg[adj_node] -= 1
                    if indeg[adj_node] == 0:
                        q.append(adj_node)

            return count != V

        adj = [[] for i in range(numCourses)]

        for first, second in prerequisites:
            adj[first].append(second)

        return not detectCycleTopo(numCourses, adj)
