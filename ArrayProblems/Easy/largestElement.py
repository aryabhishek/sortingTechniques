def find_max(arr):
    n = len(arr)

    largest = arr[0]

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    return largest

if __name__ == "__main__":
    arr = [1,2,3,4,5]

    largest_element = find_max(arr)

    print(largest_element)