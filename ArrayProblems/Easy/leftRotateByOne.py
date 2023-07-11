def left_rotate_by_one(arr):
    # arr.append(arr.pop(0))

    # return arr

    temp = arr[0]
    n = len(arr)

    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[-1] = temp

    return arr


if __name__ == "__main__":
    arr = [1,2,3,4,5,6]

    print(left_rotate_by_one(arr))