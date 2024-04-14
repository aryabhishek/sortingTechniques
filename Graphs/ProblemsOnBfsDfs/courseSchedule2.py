"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""

from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for i in range(numCourses)]

        for first, second in prerequisites:
            adj[second].append(first)

        def topoSort(V, adj):
            indeg = [0 for i in range(V)]
            ans = []

            for i in range(V):
                for node in adj[i]:
                    indeg[node] += 1

            q = deque()

            for i in range(V):
                if indeg[i] == 0:
                    q.append(i)

            while q:
                node = q[0]
                ans.append(q.popleft())
                for adj_node in adj[node]:
                    indeg[adj_node] -= 1
                    if indeg[adj_node] == 0:
                        q.append(adj_node)

            return ans

        ans = topoSort(numCourses, adj)
        return ans if len(ans) == numCourses else []
