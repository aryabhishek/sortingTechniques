from collections import deque
import sys


class Solution:

    def bfsOfGraph(self, V: int, adj: list[list[int]]) -> list[int]:
        # code here
        vis = [0]*V

        vis[0] = 1
        q = deque([0])

        bfs = []

        while q:

            node = q.popleft()

            bfs.append(node)

            for it in adj[node]:
                if vis[it] == 0:
                    vis[it] = 1
                    q.append(it)

        return bfs
