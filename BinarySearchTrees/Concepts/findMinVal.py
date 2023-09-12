def minVal(root):
    # Write your code here.
    if not root:
        return -1

    ans = root.data

    while root.left:
        if root.left:
            root = root.left
        ans = root.data

    return ans
