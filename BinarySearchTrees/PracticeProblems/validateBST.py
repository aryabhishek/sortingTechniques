def isValidBST(self, root) -> bool:
    return self.solve(root, float("-inf"), float('inf'))


def solve(self, root, min_val, max_val):
    if not root:
        return True
    
    elif not min_val < root.val < max_val:
        return False

    return self.solve(root.left, min_val, root.val) and self.solve(root.right, root.val, max_val)
