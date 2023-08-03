def linear_time(arr):
    n = len(arr)

    # for i in range(n):
    #     if (i == 0 or arr[i] > arr[i-1]) and (i == n-1 or arr[i] > arr[i+1]):
    #         return i

    # readable code which I wrote
    if n == 1:
        return arr[0]

    elif arr[0] > arr[1]:
        return arr[0]

    elif arr[-1] > arr[-2]:
        return arr[-1]

    for i in range(1, n-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            return i


def bs_solution(arr):
    n = len(arr)

    if n == 1:
        return 0

    elif arr[0] > arr[1]:
        return 0

    elif arr[-1] > arr[-2]:
        return n - 1

    low, high = 1, n - 2

    while low <= high:

        mid = (high - low)//2 + low

        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return mid

        elif arr[mid] > arr[mid-1]:  # peak is on the right side
            low = mid + 1

        else:  # peak is on the left side
            high = mid - 1

    return -1


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 5, 6, 4]

    print(bs_solution(nums))
