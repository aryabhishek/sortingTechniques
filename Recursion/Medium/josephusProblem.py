def safePos(n, k):
    # code here
    arr = [i for i in range(1, n+1)]
    k -= 1

    def solve(ar: list, k: int, idx: int) -> int:
        if len(ar) == 1:
            return ar[0]

        idx = (idx + k) % len(ar)
        ar.pop(idx)
        return solve(ar, k, idx)

    ans = solve(arr, k, 0)

    return ans


if __name__ == "__main__":
    n = 40
    k = 7

    print(safePos(n, k))
