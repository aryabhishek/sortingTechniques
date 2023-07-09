def bubbleSort(arr: [int], size: int):
    for i in range(size,1,-1):
        swaps = 0
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps += 1

        if not swaps:
            break
