def floor_sqrt(n):
    low = 1
    high = n//2

    while low <= high:

        mid = (high - low)//2 + low

        if mid * mid <= n:
            low = mid + 1

        else:
            high = mid - 1

    return high


if __name__ == "__main__":
    print(floor_sqrt(82))