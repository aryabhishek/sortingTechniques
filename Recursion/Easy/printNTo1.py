def print_n_to_1(n):
    if n == 1:
        print(1, end=" ")
        return
    print(n, end=" ")
    print_n_to_1(n-1)


def myPrint(i, n):
    if i >= n + 1:
        return
    
    myPrint(i+1, n)
    print(i, end=" ")


if __name__ == "__main__":
    print_n_to_1(10)
    myPrint(-5, -1)

