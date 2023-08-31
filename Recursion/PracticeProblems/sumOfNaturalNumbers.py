def sum_of_n(n: int) -> int:
    if n == 1:
        return 1
    
    return sum_of_n(n-1) + n


if __name__ == "__main__":
    n = 10
    print(sum_of_n(n))