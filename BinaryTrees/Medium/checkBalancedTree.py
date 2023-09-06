def isBalanced(self, root) -> bool:
    return self.find_height(root) != -1


def find_height(self, root) -> int:
    if not root:
        return 0

    left_height = self.find_height(root.left)
    if left_height == -1:
        return -1
    right_height = self.find_height(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1
