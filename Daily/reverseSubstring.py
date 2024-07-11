"""
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.
"""

from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque()

        for char in s:
            if char == ")":
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(char)

        return "".join(stack)
