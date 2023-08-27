def printS(ind: int, total: int, ds: list = []) -> None:
    if ind == n:
        if total == sum:
            print(ds)
        return

    ds.append(ar[ind])
    total += ar[ind]
    printS(ind+1, total, ds)
    ds.pop()
    total -= ar[ind]
    printS(ind+1, total, ds)


if __name__ == "__main__":
    ar = [1, 2, 1]
    n = len(ar)
    sum = 2

    printS(0, 0, [])
