class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        self.ans = image
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]
        self.n = len(image)
        self.m = len(image[0])
        init_color = image[sr][sc]
        self.dfs(image, sr, sc, color, init_color)
        return self.ans

    def dfs(self, image, row, col, new_color, init_color):
        self.ans[row][col] = new_color

        for i in range(4):
            nrow = row + self.dx[i]
            ncol = col + self.dy[i]

            if 0 <= nrow < self.n and 0 <= ncol < self.m and self.ans[nrow][ncol] == init_color and self.ans[nrow][ncol] != new_color:
                self.dfs(image, nrow, ncol, new_color, init_color)
