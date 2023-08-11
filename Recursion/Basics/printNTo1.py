def print_n_to_1(n):
    if n == 1:
        print(1, end=" ")
        return
    print(n, end=" ")
    print_n_to_1(n-1)


if __name__ == "__main__":
    print_n_to_1(10)
