def print_1_to_n(n):
    if n == 1:
        print(1, end=" ")
        return
    print_1_to_n(n-1)
    print(n, end=" ")


if __name__ == "__main__":
    print_1_to_n(10)
