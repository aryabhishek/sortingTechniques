def brute_force(arr): # TC: O(n^2), SC: O(1)
    n = len(arr)

    ans = 0

    for i in range(n):
        running_sum = 0
        for j in range(i, n):
            running_sum += arr[j]
            ans = max(ans, running_sum)

    return ans


# Kadane's Algorithm
def optimal(arr): # TC: O(n), SC: O(1)
    n = len(arr)

    ans = float("-inf")
    total = 0

    for i in range(n):
        total += arr[i]
        ans = max(ans, total)
        if total < 0:
            total = 0

    return ans


if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]

    print(optimal(arr))