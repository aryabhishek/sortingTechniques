def method1(root, val: int):
    while root and root.val != val:
        root = root.left if root.val > val else root.right

    return root


def method2(root, val: int):
    if root is None:
        return

    if root.val == val:
        return root

    if root.val > val:
        return method2(root.left, val)

    return method2(root.right, val)
