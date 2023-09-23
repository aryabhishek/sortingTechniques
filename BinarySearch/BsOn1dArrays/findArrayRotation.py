def solution(arr):
    n = len(arr)

    low = 0
    high = n - 1

    ind = 0

    while low <= high:

        mid = (high - low)//2 + low

        if arr[low] <= arr[mid]:
            if arr[low] < arr[ind]:
                ind = low
            low = mid + 1

        else:
            high = mid - 1
            if arr[mid] < arr[ind]:
                ind = mid

    return ind


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]

    print(solution(nums))