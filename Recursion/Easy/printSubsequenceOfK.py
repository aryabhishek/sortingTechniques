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


def modified_print(ind: int, total: int, ds: list = []) -> bool:
    if ind == n:
        if total == sum:
            print(ds)
            return True
        return False

    ds.append(ar[ind])
    total += ar[ind]
    if modified_print(ind+1, total, ds):
        return True
    ds.pop()
    total -= ar[ind]
    if modified_print(ind+1, total, ds):
        return True

    return False


if __name__ == "__main__":
    ar = [1, 2, 1]
    n = len(ar)
    sum = 2

    modified_print(0, 0, [])
