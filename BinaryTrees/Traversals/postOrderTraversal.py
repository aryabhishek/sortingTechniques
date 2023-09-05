def recursive(root):
    if not root:
        return
    
    recursive(root.left)
    recursive(root.right)
    print(root.val)


def iterative(root):
    pass
