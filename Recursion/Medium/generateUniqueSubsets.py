def gen_unique_subsets(s: str, out: str) -> None:
    if len(s) == 0:
        subsets.add(out)
        return

    op1 = out  # don't take
    op2 = out + s[0]  # take
    s = s.replace(s[0], "", 1)  # remove

    gen_unique_subsets(s, op1)
    gen_unique_subsets(s, op2)


if __name__ == "__main__":
    inp_str = "aab"
    subsets = set()

    gen_unique_subsets(inp_str, "")
    print(subsets)
