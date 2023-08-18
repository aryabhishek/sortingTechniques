def solve(n, ones, zeros, out) -> None:
    if n == 0:
        print(out)
        return

    if ones == zeros:
        op = out + "1"
        solve(n-1, ones+1, zeros, op)

    else:
        op1 = out + "1"
        op2 = out + "0"
        solve(n-1, ones+1, zeros, op1)
        solve(n-1, ones, zeros+1, op2)


if __name__ == "__main__":
    n = 4

    solve(n, 0, 0, '')
