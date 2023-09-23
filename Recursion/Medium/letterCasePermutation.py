def solve(inp: str, out: str) -> None:
    if not inp:
        print(out)
        return

    elif inp[0].isalpha():
        op1 = out + inp[0].lower()
        op2 = out + inp[0].upper()
        inp = inp[1:]
        solve(inp, op1)
        solve(inp, op2)

    else:
        op = out + inp[0]
        inp = inp[1:]
        solve(inp, op)


if __name__ == "__main__":
    inp = "a1B2c3D4"
    out = ''

    solve(inp, out)
