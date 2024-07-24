"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
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
