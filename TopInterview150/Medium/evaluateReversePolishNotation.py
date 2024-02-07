"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Link: https://leetcode.com/problems/evaluate-reverse-polish-notation
"""

from collections import deque


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stk = deque()

        for token in tokens:
            if token in "+-/*":
                b = stk.pop()
                a = stk.pop()
                if token == "+":
                    stk.append(a + b)
                elif token == "-":
                    stk.append(a - b)
                elif token == "*":
                    stk.append(a * b)
                else:
                    stk.append(int(float(a) / b))

            else:
                stk.append(int(token))

        return stk.pop()
