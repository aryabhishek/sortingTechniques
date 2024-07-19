"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.get_sum(root)
        return self.ans

    def get_sum(self, root):
        if not root:
            return 0

        left_sum = self.get_sum(root.left)
        right_sum = self.get_sum(root.right)

        left_and_right = left_sum + right_sum + root.val  # best path
        left_or_right = (
            max(left_sum, right_sum) + root.val
        )  # one of them could be negative

        self.ans = max(self.ans, left_and_right, left_or_right, root.val)

        return max(left_or_right, root.val)  # left_or_right could be negative
