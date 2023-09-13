def deleteNode(self, root, key: int):
    if not root:
        return

    if root.val == key:
        return self.destroyer(root)

    dummy = root

    while root:
        if root.val > key:
            if root.left and root.left.val == key:
                root.left = self.destroyer(root.left)
                break

            else:
                root = root.left

        else:
            if root.right and root.right.val == key:
                root.right = self.destroyer(root.right)
                break

            else:
                root = root.right

    return dummy


def destroyer(self, root):
    if not root.left:
        return root.right

    elif not root.right:
        return root.left

    right_child = root.right
    last_right = self.find_right(root.left)
    last_right.right = right_child
    return root.left


def find_right(self, root):
    if root.right is None:
        return root

    return self.find_right(root.right)
