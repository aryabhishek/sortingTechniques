def search(arr, k):
    l = 0
    r = len(arr) - 1

    while l <= r:

        m = (r - l)//2 + l

        if arr[m] == k:
            return m

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
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    print(search(nums, target))
