def search(arr, k):
    l = 0
    r = len(arr) - 1

    while l <= r:

        m = (l+r)//2

        if arr[m] == k:
            return m

        if arr[l] == arr[m] == arr[r]:
            l += 1
            r -= 1
            continue

        elif arr[l] <= arr[m]:
            if arr[l] <= k <= arr[m]:
                r = m - 1

            else:
                l = m + 1

        else:
            if arr[m] <= k <= arr[r]:
                l = m + 1

            else:
                r = m - 1

    return -1


if __name__ == "__main__":
    nums = [3, 1, 2, 3, 3, 3, 3]
    target = 1

    print(search(nums, target))
