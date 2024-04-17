class Solution:
    def shortest_distance(self, matrix):
        # Code here
        n = len(matrix)
        inf = 10**9

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = inf

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        # to detect cycle
        # for i in range(n):
        #     if matrix[i][i] < 0:
        #         print("There's a negative cycle")

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == inf:
                    matrix[i][j] = -1

        return matrix

        