"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

https://leetcode.com/problems/n-ary-tree-postorder-traversal
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> list[int]:
        self.ans = []
        self.traverse(root)
        return self.ans

    def traverse(self, root):
        if not root:
            return

        for child in root.children:
            self.traverse(child)
        self.ans.append(root.val)
