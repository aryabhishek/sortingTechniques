from collections import deque


def recursive(root):
    if not root:
        return

    recursive(root.left)
    print(root.val)
    recursive(root.right)


def iterative(root):
    stk = deque()
    node = root

    while True:
        if node:
            stk.append(node)
            node = node.left

        else:
            if not stk:
                break
            node = stk[-1]
            stk.pop()
            print(node.val)
            node = node.right


