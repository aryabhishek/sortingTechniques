"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

https://leetcode.com/problems/count-good-nodes-in-binary-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        self.traverse(root, root.val)
        return self.good

    def traverse(self, root, largest):
        if not root:
            return

        if root.val >= largest:
            self.good += 1
            largest = root.val

        self.traverse(root.left, largest)
        self.traverse(root.right, largest)
