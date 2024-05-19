from disjointSet import DisjointSet
from typing import List


class Solution:

    def isValid(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m

    def numOfIslands(self, n: int, m: int, operators: List[List[int]]) -> List[int]:
        # code here
        ds = DisjointSet(n * m)
        vis = [[0] * m for i in range(n)]
        count = 0
        ans = []
        for row, col in operators:
            if vis[row][col] == 1:
                ans.append(count)
                continue
            vis[row][col] = 1
            count += 1

            dr = [0, 0, 1, -1]
            dc = [1, -1, 0, 0]

            for i in range(4):
                adjr = row + dr[i]
                adjc = col + dc[i]

                if self.isValid(adjr, adjc, n, m):
                    if vis[adjr][adjc] == 1:
                        cur_node_no = row * m + col
                        adj_node_no = adjr * m + adjc
                        if ds.find_ultimate_parent(
                            cur_node_no
                        ) != ds.find_ultimate_parent(adj_node_no):
                            count -= 1
                            ds.union_by_size(cur_node_no, adj_node_no)
            ans.append(count)
        return ans
