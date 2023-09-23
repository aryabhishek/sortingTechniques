def my_print(n: int, name: str) -> None:
    if n == 1:
        print(name)
        return
    my_print(n-1, name)
    print(name)


if __name__ == "__main__":
    my_print(5, "vasu")