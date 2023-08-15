def gen_subsets(s: str, out: str) -> None:
    if len(s) == 0:
        subsets.append(out)
        return
    
    op1 = out # don't take
    op2 = out + s[0] # take
    s = s.replace(s[0], "") # remove

    gen_subsets(s, op1)
    gen_subsets(s, op2)


if __name__ == "__main__":
    string = 'abcd'
    subsets = []

    gen_subsets(string, '')
    print(subsets)