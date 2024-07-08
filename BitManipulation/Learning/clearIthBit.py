def clear_ith_bit(N: int, i: int) -> int:
    return N & ~(1 << i)


if __name__ == "__main__":
    print(clear_ith_bit(10, 2))
