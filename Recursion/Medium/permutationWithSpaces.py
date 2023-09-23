def permutation_with_spaces(inp: str, otp: str) -> None:
    if not inp:
        print(otp)
        return

    op1 = otp + "_" + inp[0]
    op2 = otp + inp[0]
    inp = inp[1:]
    permutation_with_spaces(inp, op1)
    permutation_with_spaces(inp, op2)


if __name__ == "__main__":
    i = input("Enter a string: ")
    o, i = i[0], i[1:]

    permutation_with_spaces(i, o)
