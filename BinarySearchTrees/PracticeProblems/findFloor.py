def findFloor(root, x):
    # Write your code here.

    ans = -1

    while root:

        if root.data == x:
            return x

        if x > root.data:
            ans = root.data
            root = root.right

        else: # when root.data > x
            root = root.left

    return ans