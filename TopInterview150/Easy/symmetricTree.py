"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Link: https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root is None or self.helper(root.left, root.right)

    def helper(self, left, right) -> bool:
        if left is None or right is None:
            return left == right

        elif left.val != right.val:
            return False

        return self.helper(left.left, right.right) and self.helper(
            left.right, right.left
        )
