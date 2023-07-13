def linear_search(arr, num):
    n = len(arr)

    for i in range(n):
        if arr[i] == num:
            return i
    return -1


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    print(linear_search(arr, 4))