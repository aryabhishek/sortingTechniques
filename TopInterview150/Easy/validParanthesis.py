"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Link: https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []

        for i in s:
            if i in "([{":
                stack.append(i)

            elif i in ")]}":
                if not stack:
                    return False

                top = stack.pop()

                if i is ")" and top is not "(":
                    return False

                elif i is "]" and top is not "[":
                    return False

                elif i is "}" and top is not "{":
                    return False

        return False if stack else True
