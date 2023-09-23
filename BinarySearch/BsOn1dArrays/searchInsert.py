def search_insert(arr, m):
    n = len(arr)

    low = 0
    high = n - 1

    while low <= high:

        mid = (high - low)//2 + low

        if arr[mid] == m:
            return mid

        elif arr[mid] < m:
            low = mid + 1

        else:
            high = mid - 1

    return low


if __name__ == "__main__":
    nums = [1, 2, 4, 7]
    element = 6

    print(search_insert(nums, element))
