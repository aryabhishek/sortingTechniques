import math


def sum_of_array(n, arr):
    largest = max(arr)
    arr = sorted([math.gcd(arr[i], largest) for i in range(n)])
    i, j = 0, n - 1

    while i <= j:
        arr[i] = math.gcd(arr[i], arr[j])
        i += 1
        j -= 1
    return arr


if __name__ == "__main__":
    n = 5
    arr = [5, 3, 8, 10, 64, 41]
    print(sum_of_array(n, arr))
