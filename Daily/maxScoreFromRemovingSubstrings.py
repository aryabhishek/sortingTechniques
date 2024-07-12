"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.
"""

from collections import deque


class Solution:
    ans = 0

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            s = self.remove(s, "ab", x)
            self.remove(s, "ba", y)
            return self.ans

        s = self.remove(s, "ba", y)
        self.remove(s, "ab", x)
        return self.ans

    def remove(self, s, subs, points):
        stack = deque()

        for i in range(len(s)):
            if stack and stack[-1] + s[i] == subs:
                self.ans += points
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
