def remove_duplicates(arr):

    i = 0
    n = len(arr)

    for j in range(n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i+1


if __name__ == "__main__":
    arr = [1,1,1,2,2,2,3,3,3,4,4,5,5,6]
    print(remove_duplicates(arr))
    print(arr)