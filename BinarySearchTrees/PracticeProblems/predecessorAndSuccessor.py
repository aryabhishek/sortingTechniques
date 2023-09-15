def predecessorSuccessor(root, key):

    successor = -1
    predecessor = -1

    while root:
        if root.val > key:
            predecessor = root
            root = root.right

        else:
            successor = root
            root = root.left

    return predecessor, successor
