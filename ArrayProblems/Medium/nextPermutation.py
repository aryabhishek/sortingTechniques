def next_greater_permutation(arr: list[int]) -> list[int]:

    def reverse(ar, start, end):
        while start <= end:
            ar[start], ar[end] = ar[end], ar[start]
            start += 1
            end -= 1

    n = len(arr)

    ind = -1

    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            ind = i
            break

    if ind == -1:
        reverse(arr, 0,n-1)
        return arr

    for i in range(n-1, ind, -1):
        if arr[i] > arr[ind]:
            arr[i], arr[ind] = arr[ind], arr[i]
            break

    reverse(arr, ind+1, n-1)
    return arr


if __name__ == "__main__":
    ar = [1, 3, 2]
    print(next_greater_permutation(ar))