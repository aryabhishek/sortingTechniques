from lowerBound import lower_bound
from upperBound import upper_bound


def find_first_and_last_occurance(arr, k):
    lb = lower_bound(arr, k)
    n = len(arr)

    if lb == n or arr[lb] != k:
        return [-1, -1]

    return lb, upper_bound(arr, k) - 1


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 3, 3, 3]
    target = 3

    print(find_first_and_last_occurance(nums, target))
