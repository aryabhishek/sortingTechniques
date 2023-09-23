def solve(root, maxi):
    if not root:
        return 0

    lh = solve(root.left, maxi)
    rh = solve(root.right, maxi)

    maxi = max(maxi, lh + rh)

    return 1 + max(lh, rh)
