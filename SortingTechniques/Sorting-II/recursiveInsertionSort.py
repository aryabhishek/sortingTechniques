def recursive_insertion_sort(arr, n, i):

    if (i == n):
        return
    j = i

    while j > 0 and arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1

    recursive_insertion_sort(arr, n, i+1)

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    recursive_insertion_sort(arr, len(arr), 1)
    print(arr)