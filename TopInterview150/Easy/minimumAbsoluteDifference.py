"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.res = float("inf")
        self.prev = None
        self.in_order(root)
        return self.res

    def in_order(self, root):
        if root is None:
            return

        self.in_order(root.left)

        if self.prev is not None:
            self.res = min(self.res, abs(root.val - self.prev))

        self.prev = root.val

        self.in_order(root.right)
