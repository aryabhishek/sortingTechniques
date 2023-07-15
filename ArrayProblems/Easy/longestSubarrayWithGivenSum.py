def solution(a, k):
    left, right = 0, 0
    n = len(a)

    total = a[0]
    ans = 0

    while right < n:

        while left <= right and total > k:
            total -= a[left]
            left += 1

        if total == k:
            ans = max(ans, right - left + 1)

        right += 1
        if right < n:
            total += a[right]

    return ans


if __name__ == "__main__":
    arr = [1,2,3,3,4,6,6,7,5,1,1,1,1,1,4]
    k = 12

    print(solution(arr, k))