from typing import List


def longestBitonicSubsequence(arr: List[int], n: int) -> int:
    # write your code here
    dp_left = [1] * n
    dp_right = [1] * n

    for i in range(n):
        for prev in range(i):
            if arr[i] > arr[prev] and dp_left[prev] + 1 > dp_left[i]:
                dp_left[i] = dp_left[prev] + 1

    for i in range(n - 1, -1, -1):
        for prev in range(n - 1, i, -1):
            if arr[i] > arr[prev] and dp_right[prev] + 1 > dp_right[i]:
                dp_right[i] = dp_right[prev] + 1

    bitonic = [dp_left[i] + dp_right[i] - 1 for i in range(n)]

    return max(bitonic)
