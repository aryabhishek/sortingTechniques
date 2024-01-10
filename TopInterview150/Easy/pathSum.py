"""
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
Link: https://leetcode.com/problems/path-sum/?envType=study-plan-v2&envId=top-interview-150
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.ans = 0
        if root:
            self.solve(root, 0, targetSum)
        return self.ans

    def solve(self, root, total, goal):
        if not root:
            return
        total += root.val
        if not root.left and not root.right and total == goal:
            self.ans = 1
            return

        self.solve(root.left, total, goal)
        self.solve(root.right, total, goal)
