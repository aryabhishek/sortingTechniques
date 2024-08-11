"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

https://leetcode.com/problems/path-sum-iii/
"""

from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        self.target = targetSum
        self.traverse(root)
        return self.paths

    def traverse(self, root):
        if not root:
            return

        self.solve(root, 0)
        self.traverse(root.left)
        self.traverse(root.right)

    def solve(self, root, cur_sum):
        if not root:
            return
        self.solve(root.left, cur_sum + root.val)
        self.solve(root.right, cur_sum + root.val)
        if cur_sum + root.val == self.target:
            self.paths += 1


class OptimalSolution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        self.target = targetSum
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1
        self.traverse(root, 0)
        return self.paths

    def traverse(self, root, cur_sum):
        if not root:
            return
        cur_sum += root.val
        self.paths += self.lookup[cur_sum]
        self.lookup[cur_sum + self.target] += 1
        self.traverse(root.left, cur_sum)
        self.traverse(root.right, cur_sum)
        self.lookup[cur_sum + self.target] -= 1
