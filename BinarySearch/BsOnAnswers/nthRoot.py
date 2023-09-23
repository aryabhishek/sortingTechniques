def my_pow(x, n): # TC: log(n)
    if n == 0:
        return 1

    if n < 0:
        return my_pow(1/x, -n)

    if n % 2 == 0:
        return my_pow(x*x, n/2)

    return x * my_pow(x*x, (n-1)/2)


def nth_root(n: int, m: int) -> int: # TC: log(n) * log(m)
    low, high = 1, m//2

    while low <= high:

        mid = (high - low)//2 + low
        mid_pow = my_pow(mid, n)

        if mid_pow == m:
            return mid

        elif mid_pow < m:
            low = mid + 1

        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    n, m = 3, 27

    print(nth_root(n, m))