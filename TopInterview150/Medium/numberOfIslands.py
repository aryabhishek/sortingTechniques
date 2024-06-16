"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def is_valid(x, y, mat):
            return 0 <= x < len(mat) and 0 <= y < len(mat[0])

        def dfs(i, j, mat, vis):
            vis[i][j] = 1

            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]

            for _ in range(4):
                new_x = dx[_] + i
                new_y = dy[_] + j

                if (
                    is_valid(new_x, new_y, mat)
                    and vis[new_x][new_y] == 0
                    and mat[new_x][new_y] == "1"
                ):
                    dfs(new_x, new_y, mat, vis)

        m = len(grid)
        n = len(grid[0])
        vis = [[0] * n for i in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and vis[i][j] == 0:
                    dfs(i, j, grid, vis)
                    ans += 1

        return ans
