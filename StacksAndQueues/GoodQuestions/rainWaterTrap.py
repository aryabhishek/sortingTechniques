def trap(arr: list[int]) -> int:
    n = len(arr)
    mxl = [arr[0]] * n
    mxr = [arr[-1]] * n

    for i in range(1, n):
        mxl[i] = max(mxl[i - 1], arr[i])

    for i in range(n - 2, -1, -1):
        mxr[i] = max(mxr[i + 1], arr[i])

    water = [min(mxl[i], mxr[i]) - arr[i] for i in range(n)]

    return sum(water)

if __name__ == "__main__":
    height = [4,2,0,3,2,5]

    print(trap(height))
