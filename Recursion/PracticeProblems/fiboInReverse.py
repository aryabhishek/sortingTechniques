def fibo(n: int) -> int:
    if n <= 1:
        return n

    return fibo(n-1) + fibo(n-2)


def print_fibo_in_reverse(n: int) -> None:
    if n == 0:
        return print(0)

    print(fibo(n))
    print_fibo_in_reverse(n-1)


if __name__ == "__main__":
    n = 10
    print_fibo_in_reverse(n)
