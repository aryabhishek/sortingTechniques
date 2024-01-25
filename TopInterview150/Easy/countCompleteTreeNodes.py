"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Link: https://leetcode.com/problems/count-complete-tree-nodes
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight == rightHeight:
            return 2**leftHeight + self.countNodes(root.right)
        else:
            return 2**rightHeight + self.countNodes(root.left)

    def getHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
