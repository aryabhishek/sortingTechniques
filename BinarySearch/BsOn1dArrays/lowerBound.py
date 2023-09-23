def lower_bound(arr, x):
    n = len(arr)
    l = 0
    r = n - 1

    ans = n

    while l <= r:

        m = (l+r) // 2

        if arr[m] >= x:
            ans = m
            r = m - 1

        elif arr[m] < x:
            l = m + 1

    return ans


if __name__ == "__main__":
    import bisect
    nums = [1, 2, 2, 3]
    print(bisect.bisect_left(nums, 0))
    print(lower_bound(nums, 0))
