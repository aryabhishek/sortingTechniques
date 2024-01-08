"""
Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [low, high].
Link: https://leetcode.com/problems/range-sum-of-bst/?envType=daily-question&envId=2024-01-08
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stk, sum = [root], 0
        while stk:
            node = stk.pop()
            if node:
                if node.val > low:
                    stk.append(node.left)
                if node.val < high:
                    stk.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum
