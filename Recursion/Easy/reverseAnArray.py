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


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5]
    reverse(ar)
    print(ar)