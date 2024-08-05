"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

https://leetcode.com/problems/guess-number-higher-or-lower/
"""


def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:

        l = 1
        r = n

        while l <= r:
            m = (l + r) // 2
            guessed_number = guess(m)

            if guessed_number == 0:
                return m

            elif guessed_number == -1:
                r = m - 1

            elif guessed_number == 1:
                l = m + 1
