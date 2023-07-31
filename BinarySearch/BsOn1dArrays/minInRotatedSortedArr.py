def my_solution(arr):
    n = len(arr)

    low = 0
    high = n - 1

    ans = arr[0]

    while low <= high:

        mid = (high - low)//2 + low

        ans = min(ans, arr[low], arr[high], arr[mid])

        if arr[low] < arr[mid]:
            if ans > arr[low] and ans <= arr[high]:
                high = mid - 1

            else:
                low = mid + 1

        else:
            if ans > arr[mid] + 1 and ans <= arr[low]:
                low = mid + 1

            else:
                high = mid - 1

    return ans


def optimal(arr): # same solution but the code is much cleaner than mine(no unnecessary checks)
    n = len(arr)

    low = 0
    high = n - 1

    ans = arr[0]

    while low <= high:

        mid = (high - low)//2 + low

        if arr[low] <= arr[mid]:
            ans = min(ans, arr[low])
            low = mid + 1

        else:
            high = mid - 1
            ans = min(ans, arr[mid])

    return ans


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]

    print(optimal(nums))