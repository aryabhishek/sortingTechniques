"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Link: https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        return (
            p.val == q.val
            and (self.isSameTree(p.left, q.left))
            and (self.isSameTree(p.right, q.right))
        )
