def insert(ar: list, ele: object) -> None:
    if not ar:
        ar.append(ele)
        return
    
    last = ar.pop()
    insert(ar, ele)
    ar.append(last)


def reverse(arr: list) -> None:
    if len(arr) == 1:
        return
    
    last = arr.pop()
    reverse(arr)
    insert(arr, last)


# two variables
def swap_reverse(arr, l, r):
    if l >= r:
        return
    
    arr[l], arr[r] = arr[r], arr[l]
    swap_reverse(arr, l+1, r-1)


# one variable
def reverse_arr(arr, i):
    if i >= len(arr)//2:
        return
    
    arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    reverse_arr(arr, i+1)


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5]
    reverse_arr(ar, 0)
    print(ar)