"""
A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people.  A square matrix mat is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.

https://www.geeksforgeeks.org/problems/the-celebrity-problem/1
"""


class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        top, bot = 0, n - 1

        while top < bot:
            if mat[top][bot] == 1:
                top += 1
            elif mat[bot][top] == 1:
                bot -= 1
            else:
                top += 1
                bot -= 1

        if top > bot:
            return -1

        for i in range(n):
            if i == top:
                continue
            if mat[top][i] != 0 or mat[i][top] != 1:
                return -1

        return top
