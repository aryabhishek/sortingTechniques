from collections import deque

def is_leaf(root):
    return not root.left and not root.right


def add_left_boundary(root, ds):
    cur = root.left

    while cur:
        if not is_leaf(cur):
            ds.append(cur.val)

        if cur.left:
            cur = cur.left
        else:
            cur = cur.right


def add_right_boundary(root, ds):
    cur = root.right
    temp = deque()

    while cur:
        if not is_leaf(cur):
            temp.append(cur.val)

        if cur.right:
            cur = cur.right
        else:
            cur = cur.left

    while temp:
        ds.append(temp.pop())


def add_leaves(root, ds):
    if is_leaf(root):
        ds.append(root.val)
        return
    
    if root.left:
        add_leaves(root.left, ds)

    if root.right:
        add_leaves(root.right, ds)



def traverseBoundary(root):
    # Write your code here.
    res = []
    if not root:
        return res

    if not is_leaf(root):
        res.append(root.val)

    add_left_boundary(root, res)
    add_leaves(root, res)
    add_right_boundary(root, res)

    return res
