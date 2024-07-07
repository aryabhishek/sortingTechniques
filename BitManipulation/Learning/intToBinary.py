def int_to_bin(n: int) -> str:
    """Converts an integer to its binary representation."""
    res = []
    while n > 0:
        if n % 2 == 1:
            res.append("1")
        else:
            res.append("0")
        n = n // 2
    return "".join(res[::-1])


if __name__ == "__main__":
    print(int_to_bin(13))
