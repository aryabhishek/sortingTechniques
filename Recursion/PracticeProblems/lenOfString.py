def length_of(s: str) -> int:
    if s == "":
        return 0
    s = s[1:] # removing first element
    return length_of(s) + 1


if __name__ == "__main__":
    string = 'Hello World!'
    print(length_of(string))
