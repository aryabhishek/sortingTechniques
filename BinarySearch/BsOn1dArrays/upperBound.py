def upper_bound(arr, x):
    n = len(arr)
    l = 0
    r = n - 1

    ans = n

    while l <= r:

        m = (l+r) // 2

        if arr[m] > x:
            ans = m
            r = m - 1

        elif arr[m] <= x:
            l = m + 1

    return ans


if __name__ == "__main__":
    nums = [1, 4, 7, 8, 10]
    target = 7

    print(upper_bound(nums, target))