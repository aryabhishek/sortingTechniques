"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return

        self.ans = []
        q = deque()
        q.append(root)
        self.solve(q)
        return self.ans

    def solve(self, que) -> None:
        flag = True  # True -> left to right // False -> right to left

        while que:
            size = len(que)
            temp = [None] * size

            for i in range(size):
                node = que[0]
                que.popleft()

                index = i if flag else size - i - 1

                temp[index] = node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            flag = not flag

            self.ans.append(temp)
