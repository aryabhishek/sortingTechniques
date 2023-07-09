def bubbleSort(arr, idx):
    if idx == 0:
        return
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    bubbleSort(arr, idx - 1)

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    n= len(arr)
    bubbleSort(arr,n)
    print(arr)