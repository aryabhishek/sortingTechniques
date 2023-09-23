from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        total_oranges = 0
        rotten_oranges = 0
        minutes = 0

        # elements of q: [(row, col), time]
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    total_oranges += 1

                if grid[i][j] == 2:
                    q.append(((i, j), 0))
                    visited[i][j] = 1
                    rotten_oranges += 1

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while q:

            row = q[0][0][0]
            col = q[0][0][1]
            time = q.popleft()[1]
            minutes = max(time, minutes)

            for i in range(4):
                x = row + dx[i]
                y = col + dy[i]

                if 0 <= x < n and 0 <= y < m and visited[x][y] != 1 and grid[x][y] == 1:
                    q.append(((x, y), time + 1))
                    visited[x][y] = 1
                    rotten_oranges += 1

        return minutes if rotten_oranges == total_oranges else -1


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

    obj = Solution()
    print(obj.orangesRotting(grid))