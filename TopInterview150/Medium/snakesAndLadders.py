"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.
"""

from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        def get_coor(num, n):
            row_top = (num - 1) // n
            row_bot = n - 1 - row_top
            col = (num - 1) % n

            if row_top % 2 == 0:
                return row_bot, col
            else:
                return row_bot, n - 1 - col

        n = len(board)
        steps = 0
        q = deque([1])
        vis = set([1])

        while q:
            size = len(q)
            for _ in range(size):
                cell = q.popleft()
                if cell == n * n:
                    return steps

                for i in range(1, 7):
                    next_cell = cell + i
                    if next_cell > n * n:
                        break
                    row, col = get_coor(next_cell, n)
                    if (row, col) in vis:
                        continue
                    vis.add((row, col))
                    if board[row][col] == -1:
                        q.append(next_cell)
                    else:
                        q.append(board[row][col])
            steps += 1

        return -1
