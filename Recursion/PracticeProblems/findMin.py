def find_min(arr: list, idx: int = 0, temp: int = None) -> int:
    if idx == len(arr):
        return temp

    if temp is None or temp > arr[idx]:
        temp = arr[idx]

    return find_min(arr, idx + 1, temp)


if __name__ == "__main__":
    ar = [1, 2, 3, -10, 4, 5]

    print(find_min(ar))
