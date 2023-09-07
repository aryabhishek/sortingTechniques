def solve(root, ans=float('-inf')):
    if not root:
        return 0

    lsum = max(0, solve(root.left, ans)) # if the sum is -ve, consider it as 0
    rsum = max(0, solve(root.right, ans))

    ans = max(ans, lsum + rsum + root.val)

    return root.val + max(lsum, rsum)
