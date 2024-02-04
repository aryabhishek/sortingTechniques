"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.flatter(root)

    def flatter(self, node):
        if not node:
            return

        self.flatter(node.right)
        self.flatter(node.left)
        node.right = self.prev
        node.left = None
        self.prev = node
