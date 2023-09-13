def kthSmallest(self, root, k: int) -> int:
    self.ans = 0
    self.k = k

    self.solve(root)
    return self.ans


def solve(self, root):
    if not root or self.k == 0:
        return

    self.solve(root.left)
    if self.k == 1:
        self.ans = root.val
        self.k = 0
        return
    else:
        self.k -= 1

    self.solve(root.right)
