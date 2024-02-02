"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Link: https://leetcode.com/problems/generate-parentheses
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.ans = []
        self.gen_balanced_parentheses(n,n,'')
        return self.ans

    def gen_balanced_parentheses(self, open: int, close: int, out: str) -> None: 
        if open == close == 0:
            self.ans.append(out)
            return

        if open == close:
            op = out + '('
            self.gen_balanced_parentheses(open-1, close, op)

        else:
            if open != 0:
                op1 = out + '('
                op2 = out + ')'
                self.gen_balanced_parentheses(open-1, close, op1)
                self.gen_balanced_parentheses(open, close-1, op2)
            else:
                op = out + ')'
                self.gen_balanced_parentheses(open, close-1, op)
