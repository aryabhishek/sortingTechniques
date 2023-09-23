from collections import deque

def recursive(root):
    if not root:
        return
    
    recursive(root.left)
    recursive(root.right)
    print(root.val)


def iterative(root): # two stacks
    stk1 = deque()
    stk2 = deque()
    stk1.append(root)
    while stk1:
        node = stk1[-1]
        stk1.pop()
        stk2.append(node)
        if node.left: stk1.append(node.left)
        if node.right: stk1.append(node.right)

    while stk2:
        data = stk2[-1].val
        stk2.pop()
        print(data)
