def clear_last_set_bit(N: int) -> int:
    return N & (N - 1)


if __name__ == "__main__":
    print(clear_last_set_bit(10))
