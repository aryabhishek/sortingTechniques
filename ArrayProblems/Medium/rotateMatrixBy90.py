"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

https://leetcode.com/problems/rotate-image
"""

def rotate(matrix: list[list[int]]) -> None: # TC: O(n^2), SC: O(n^2)

    n = len(matrix)

    ans = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ans[j][n-i-1] = matrix[i][j]

    # for i in range(n):
    #     for j in range(n):
    #         matrix[i][j] = ans[i][j]

    matrix[::] = ans # Python is op


def optimal(matrix): # TC: O(n^2), SC: O(1)
    n = len(matrix)

    for i in range(n-1):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    # print original matrix
    for row in matrix:
        for ele in row:
            print(ele, end=" ")
        print()

    print()
    optimal(matrix)
    
    # print rotated matrix
    for row in matrix:
        for ele in row:
            print(ele, end=" ")
        print()
