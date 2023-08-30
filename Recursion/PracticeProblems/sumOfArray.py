def sum_arr(arr: list, idx: int, total: int) -> int:
    if idx == n:
        return total

    return sum_arr(arr, idx+1, total+arr[idx])


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5]
    n = len(ar)

    print(sum_arr(ar, 0, 0))
