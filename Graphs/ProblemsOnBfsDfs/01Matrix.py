from collections import deque
import numpy as np

def nearest(mat, n, m):
    # Write your code here.

    vis = [[0]*m for _ in range(n)]
    ans = [[0]*m for _ in range(n)]
    q = deque()  # pair: ((row, col), steps)

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                vis[i][j] = 1
                q.append(((i, j), 0))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        row = q[0][0][0]
        col = q[0][0][1]
        steps = q.popleft()[1]

        ans[row][col] = steps

        for i in range(4):
            n_row = row + dx[i]
            n_col = col + dy[i]

            if 0 <= n_row < n and 0 <= n_col < m and vis[n_row][n_col] == 0:
                vis[n_row][n_col] = 1
                q.append(((n_row, n_col), steps+1))

    return ans


if __name__ == "__main__":
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    
    print(np.array(nearest(mat, 3, 3)))