class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.mid = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        self.in_order(root)

        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val

        else:
            self.first.val, self.mid.val = self.mid.val, self.first.val

    def in_order(self, root):
        if not root:
            return

        self.in_order(root.left)

        if self.prev and root.val < self.prev.val:

            if not self.first:
                self.first = self.prev
                self.mid = root

            else:
                self.second = root

        self.prev = root

        self.in_order(root.right)
