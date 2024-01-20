"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Link: https://leetcode.com/problems/binary-search-tree-iterator/
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stk = deque()
        self.push_all(root)

    def next(self) -> int:
        node = self.stk.pop()
        self.push_all(node.right)
        return node.val

    def hasNext(self) -> bool:
        return True if self.stk else False

    def push_all(self, node):
        while node:
            self.stk.append(node)
            node = node.left
