def solve(n, arr):
    pre_sum = [arr[0]] * n
    for i in range(1, n):
        pre_sum[i] = pre_sum[i - 1] + arr[i]

    suff_sum = [arr[-1]] * n
    for i in range(n - 2, -1, -1):
        suff_sum[i] = suff_sum[i + 1] + arr[i]
    res = []
    for i in range(n):
        if i == 0:
            dist = suff_sum[1] - arr[-1]
        elif i == n - 1:
            dist = pre_sum[n - 2] - arr[0]
        else:
            dist = (
                pre_sum[i - 1]
                + suff_sum[i + 1]
                - (arr[0] if arr[0] > arr[-1] else arr[-1])
            )
        res.append(dist)

    return res


if __name__ == "__main__":
    n = 3
    arr = [1, 3, 8]
    print(solve(n, arr))
