"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
"""


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        self.adj = [[] for _ in range(n)]

        for a, b in connections:
            self.adj[a].append([b, 1])
            self.adj[b].append([a, 0])

        self.flips = 0
        self.dfs(0, -1)
        return self.flips

    def dfs(self, start, parent):
        for node, is_real in self.adj[start]:
            if node != parent:
                if is_real:
                    self.flips += 1
                self.dfs(node, start)


if __name__ == "__main__":
    solution = Solution()
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    print(solution.minReorder(n, connections))
