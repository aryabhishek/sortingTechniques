from collections import deque


class BSTIterator:

    def __init__(self, root, rev):
        self.reverse = rev
        self.stk = deque()
        self.root = root
        self.push_all(root)

    def next(self) -> int:
        node = self.stk.pop()
        if not self.reverse:
            self.push_all(node.right)
        else:
            self.push_all(node.left)
        return node.val

    def hasNext(self) -> bool:
        return True if self.stk else False

    def push_all(self, node):
        while node:
            self.stk.append(node)
            if not self.reverse:
                node = node.left
            else:
                node = node.right


class Solution:
    def findTarget(self, root, k: int) -> bool:
        if not root:
            return False

        left = BSTIterator(root, False)
        right = BSTIterator(root, True)

        i = left.next()
        j = right.next()

        while i < j:
            if i + j == k:
                return True

            elif i + j < k:
                i = left.next()

            else:
                j = right.next()

        return False
