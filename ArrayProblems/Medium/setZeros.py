def mark_row(mat, m, row):
    for j in range(m):
        if mat[row][j] != 0:
            mat[row][j] = -1


def mark_col(mat, n, col):
    for i in range(n):
        if mat[i][col] != 0:
            mat[i][col] = -1


def set_zeroes(matrix: list[list[int]]) -> None: # TC: around O(n^3), SC: O(1)
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                mark_row(matrix, m, i)
                mark_col(matrix, n, j)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0


def better(matrix): # TC: O(2*n*m), SC: O(n+m)
    n = len(matrix)
    m = len(matrix[0])

    col = [0]*m
    row = [0]*n

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0


def optimal(matrix): # TC: O(2*n*m), SC: O(1)
    n = len(matrix)
    m = len(matrix[0])
    col0 = 1

    # Step 1: marking first row and first column
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0

                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # Step 2: solving for the smaller matrix
    for i in range(1, n):
        for j in range(1, m):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    # Step 3: solving for the first row which is dependent upon matrix[0][0]
    if not matrix[0][0]:
        for j in range(m):
            matrix[0][j] = 0
    
    # Step 4: solving for the first col which is dependent upon col0
    if not col0:
        for i in range(n):
            matrix[i][0] = 0


if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

    optimal(matrix)

    for row in matrix:
        for ele in row:
            print(ele, end='  ')
        print()