"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def solve(l, r):
            if l > r:
                return

            mid = l + (r - l) // 2
            root = TreeNode(nums[mid])
            root.left = solve(l, mid - 1)
            root.right = solve(mid + 1, r)
            return root

        return solve(0, len(nums) - 1)
