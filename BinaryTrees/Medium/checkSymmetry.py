def isSymmetric(root) -> bool:
    return root is None or helper(root.left, root.right)


def helper(left, right) -> bool:
    if left is None or right is None:
        return left == right

    elif left.val != right.val:
        return False

    return helper(left.left, right.right) and helper(left.right, right.left)
