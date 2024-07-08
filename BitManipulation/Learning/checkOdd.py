def check_odd(N: int) -> bool:
    return bool(N & 1)


if __name__ == "__main__":
    print(check_odd(5))