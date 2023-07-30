def binary_search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l+r)//2

        if nums[m] == target:
            return m

        elif nums[m] < target:
            l = m + 1

        else:
            r = m - 1

    return -1


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 8, 9, 1, 3]
    target = 9

    print(binary_search(arr, target))
