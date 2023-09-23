def insert(arr: list, value: int) -> None:
    if len(arr) == 0 or arr[-1] <= value:
        arr.append(value)
        return

    last_ele = arr.pop()

    insert(arr, value)
    arr.append(last_ele)


def sort(arr: list) -> None:
    if len(arr) <= 1:
        return

    last_ele = arr.pop()

    sort(arr)
    insert(arr, last_ele)


if __name__ == "__main__":
    nums = [5, 4, 3, 8, 2, 1, 69]

    sort(nums)

    print(nums)
