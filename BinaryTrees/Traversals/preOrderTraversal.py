from collections import deque

def pre_order(root) -> None:
    if not root:
        return

    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


def iterative(root):
    stk = deque()
    stk.append(root)

    while stk:
        node = stk[-1]
        stk.pop()
        print(node.val)

        if node.right:
            stk.append(node.right)

        if node.left:
            stk.append(node.left)
