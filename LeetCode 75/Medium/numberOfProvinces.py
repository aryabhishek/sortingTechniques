"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

https://leetcode.com/problems/number-of-provinces/
"""


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        self.vis = [0] * n
        adj_ls = [[] for _ in range(n)]
        count = 0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj_ls[i].append(j)
                    adj_ls[j].append(i)

        for i in range(n):
            if self.vis[i] == 0:
                self.dfs(i, adj_ls)
                count += 1

        return count

    def dfs(self, node, adj):
        self.vis[node] = 1

        for it in adj[node]:
            if self.vis[it] == 0:
                self.dfs(it, adj)
