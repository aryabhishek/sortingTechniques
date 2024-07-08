def toggle_ith_bit(N: int, i: int) -> int:
    return N ^ (1 << i)


if __name__ == "__main__":
    print(toggle_ith_bit(10, 3))
