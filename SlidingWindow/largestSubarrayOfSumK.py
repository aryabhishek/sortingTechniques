def solve(arr, k): # for arr of +ve nums
    n = len(arr)
    ans, r_sum = 0, 0
    i, j = 0, 0

    while j < n:
        r_sum += arr[j]

        if r_sum < k:
            j += 1

        elif r_sum == k:
            ans = max(ans, j - i + 1)
            r_sum -= arr[i]
            i += 1
            j += 1

        else:
            while r_sum > k:
                r_sum -= arr[i]
                i += 1
            j += 1
    return ans


if __name__ == "__main__":
    a = [4, 1, 1, 1, 2, 3, 5]
    print(solve(a, 5))
 