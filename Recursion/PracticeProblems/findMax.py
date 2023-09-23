def find_max(arr: list, idx: int = 0, temp: int = None) -> int:
    if idx == len(arr):
        return temp

    if temp is None or temp < arr[idx]:
        temp = arr[idx]

    return find_max(arr, idx + 1, temp)


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 69, 54, 32, -100]
    print(find_max(ar))
