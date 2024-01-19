"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans = 0
        self.k = k

        self.solve(root)
        return self.ans

    def solve(self, root):
        if not root or self.k == 0:
            return

        self.solve(root.left)
        if self.k == 1:
            self.ans = root.val
            self.k = 0
            return
        else:
            self.k -= 1

        self.solve(root.right)
