def fact(n: int) -> int:
    if n == 0:
        return 1
    
    return fact(n-1) * n


if __name__ == "__main__":
    n = 5

    print(fact(n))