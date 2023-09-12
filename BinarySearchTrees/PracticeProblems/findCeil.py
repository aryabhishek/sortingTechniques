def findCeil(root, x):
    # Write your code here.

    ans = -1

    while root:

        if root.data == x:
            return x

        if root.data < x:
            root = root.right

        else:  # when root.data > x
            ans = root.data
            root = root.left

    return ans
