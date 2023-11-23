def max_sum_subarr(arr, k):
    max_sum = float('-inf')
    i = 0 # start
    j = 0 # end
    r_sum = 0

    while j < len(arr):
        r_sum += arr[j]

        if j == k+i-1:
            max_sum = max(max_sum, r_sum)
            r_sum -= arr[i]
            i += 1
        j += 1

    return max_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sum_subarr(arr, 6))