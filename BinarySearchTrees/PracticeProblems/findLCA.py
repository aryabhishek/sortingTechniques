def iterative(root, p, q):

    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right

        elif p.val < root.val and q.val < root.val:
            root = root.left

        else:
            return root


def lowestCommonAncestor(self, root, p, q):
    if not root:
        return

    cur = root.val

    if cur < p.val and cur < q.val:
        return self.lowestCommonAncestor(root.right, p, q)

    if cur > p.val and cur > q.val:
        return self.lowestCommonAncestor(root.left, p, q)

    return root
