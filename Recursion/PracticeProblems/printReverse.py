def print_reverse(s: str) -> None:
    if len(s) == 1:
        return print(s, end="")
    print(s[-1], end='')
    print_reverse(s[:-1])


if __name__ == "__main__":
    string = "aggin olleh"

    print_reverse(string)
