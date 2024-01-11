"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Link: https://leetcode.com/problems/validate-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.solve(root, float("-inf"), float("inf"))

    def solve(self, root, min_val, max_val):
        if not root:
            return True

        elif not min_val < root.val < max_val:
            return False

        return self.solve(root.left, min_val, root.val) and self.solve(
            root.right, root.val, max_val
        )
