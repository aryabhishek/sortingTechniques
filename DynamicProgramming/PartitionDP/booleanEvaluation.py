"""
You are given an expression 'exp' in the form of a string where operands will be : (TRUE or FALSE), and operators will be : (AND, OR or XOR).



Now you have to find the number of ways we can parenthesize the expression such that it will evaluate to TRUE.



As the answer can be very large, return the output modulo 1000000007.



Note :

‘T’ will represent the operand TRUE.
‘F’ will represent the operand FALSE.
‘|’ will represent the operator OR.
‘&’ will represent the operator AND.
‘^’ will represent the operator XOR.
Example :

Input: 'exp’ = "T|T & F".

Output: 1

Explanation:
There are total 2  ways to parenthesize this expression:
    (i) (T | T) & (F) = F
    (ii) (T) | (T & F) = T
Out of 2 ways, one will result in True, so we will return 1.

https://www.naukri.com/code360/problems/boolean-evaluation_1214650
"""


def evaluateExp(exp: str) -> int:
    n = len(exp)
    mod = 1000000007

    dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(n):
            if i > j:
                continue

            for isTrue in range(2):
                if i == j:
                    if isTrue == 1:
                        dp[i][j][isTrue] = int(exp[i] == "T")
                    else:
                        dp[i][j][isTrue] = int(exp[i] == "F")
                    continue

                ways = 0
                for ind in range(i + 1, j, 2):
                    lT = dp[i][ind - 1][1]
                    lF = dp[i][ind - 1][0]
                    rT = dp[ind + 1][j][1]
                    rF = dp[ind + 1][j][0]

                    if exp[ind] == "&":
                        if isTrue:
                            ways = (ways + (lT * rT) % mod) % mod
                        else:
                            ways = (
                                ways
                                + (lF * rT) % mod
                                + (lT * rF) % mod
                                + (lF * rF) % mod
                            ) % mod
                    elif exp[ind] == "|":
                        if isTrue:
                            ways = (
                                ways
                                + (lF * rT) % mod
                                + (lT * rF) % mod
                                + (lT * rT) % mod
                            ) % mod
                        else:
                            ways = (ways + (lF * rF) % mod) % mod
                    else:
                        if isTrue:
                            ways = (ways + (lF * rT) % mod + (lT * rF) % mod) % mod
                        else:
                            ways = (ways + (lF * rF) % mod + (lT * rT) % mod) % mod

                dp[i][j][isTrue] = ways

    return dp[0][n - 1][1]
