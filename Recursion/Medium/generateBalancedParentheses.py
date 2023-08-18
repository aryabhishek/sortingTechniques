def gen_balanced_parentheses(open: int, close: int, out: str) -> None: # wrote this myself without watching the video
    if open == close == 0:
        print(out)
        return

    if open == close:
        op = out + '('
        gen_balanced_parentheses(open-1, close, op)

    else:
        if open != 0:
            op1 = out + '('
            op2 = out + ')'
            gen_balanced_parentheses(open-1, close, op1)
            gen_balanced_parentheses(open, close-1, op2)
        else:
            op = out + ')'
            gen_balanced_parentheses(open, close-1, op)


if __name__ == "__main__":
    n = 4
    gen_balanced_parentheses(n, n, '')
