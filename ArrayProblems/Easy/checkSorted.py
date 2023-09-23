def is_sorted(arr):
    """Returns 1 if the array is sorted in ascending order otherwise 0"""

    n = len(arr)

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
        
    return True


if __name__ == "__main__":
    arr = [1,2,3,6,5]
    print("Sorted") if is_sorted(arr) else print("Not Sorted")  