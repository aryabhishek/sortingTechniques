def find_len(s: str, idx) -> int:  # Method I
    try:
        s[idx]

    except:  # Exception will occur only if we go out of bounds
        return idx

    else:
        return find_len(s, idx + 1)


def length_of(s: str, idx: int) -> int: # This will not work in C and C++
    if s[idx] == s[-1]:
        return idx + 1

    return length_of(s, idx + 1)


if __name__ == "__main__":
    string = 'Hello World!'
    print(find_len(string, 0))
    print(length_of(string, 0))
