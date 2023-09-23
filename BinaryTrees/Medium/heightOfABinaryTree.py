def find_height(root) -> int:
    if not root:
        return 0

    left_height = find_height(root.left)
    right_height = find_height(root.right)

    return max(left_height, right_height) + 1
