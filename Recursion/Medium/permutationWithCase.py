def solve(inp: str, out: str) -> None:
    if not inp:
        print(out)
        return

    op1 = out + inp[0]
    op2 = out + inp[0].upper()
    inp = inp[1:]
    solve(inp, op1)
    solve(inp, op2)
    return


if __name__ == "__main__":
    inp = "ab"
    out = ""

    solve(inp, out)
