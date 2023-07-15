def solution(a, k):
    i, j = 0, 0
    n = len(a)

    total = a[0]
    ans = 0

    while j < n:

        while i <= j and total > k:
            total -= a[i]
            i += 1

        if total == k:
            ans = max(ans, j - i + 1)

        j += 1
        if j < n:
            total += a[j]

    return ans


if __name__ == "__main__":
    arr = [1,2,3,3,4,6,6,7,5,1,1,1,1,1,4]
    k = 12

    print(solution(arr, k))