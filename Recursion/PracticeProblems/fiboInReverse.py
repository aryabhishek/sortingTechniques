import os

def fibo(n: int) -> int:
    if n <= 1:
        return n
    fib = fibo(n-1) + fibo(n-2)
    print(fib)
    return fib


def fib2(n: int, x: int, y: int) -> None:
    if n <= 1:
        print(x)
        return
    fib2(n - 1, y, x + y)
    print(x)


def print_fibo_in_reverse(n: int) -> None:
    if n == 0:
        return print(0)

    print(fibo(n))
    print_fibo_in_reverse(n-1)


if __name__ == "__main__":
    n = 10
    # print_fibo_in_reverse(n)
    os.system("cls")
    fib2(n, 0, 1)
    my_fib(n, 0, 1)
