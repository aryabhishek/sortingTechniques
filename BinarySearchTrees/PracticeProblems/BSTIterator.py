from collections import deque


class BSTIterator:

    def __init__(self, root):
        self.stk = deque()
        self.root = root
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
