# parameterised

def param_sum_of_n(total, n):
    if n == 0:
        print(total)
        return

    param_sum_of_n(total + n, n-1)


# functional
def sum_of_n(n):
    if n == 1:
        return 1

    return n + sum_of_n(n-1)


if __name__ == "__main__":
    print(sum_of_n(9))
    param_sum_of_n(0, 9)
