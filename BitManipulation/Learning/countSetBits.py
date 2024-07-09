def count_set_bits(N: int) -> int:
    """Count the number of set bits in the binary representation of N."""
    count = 0
    while N > 0:
        count += N & 1
        N >>= 1
    return count

def count_set_bits_2(N: int) -> int:
    """Count the number of set bits in the binary representation of N."""
    count = 0
    while N != 0: # N == 0 means we have cleard all set bits
        N = N & (N - 1) # clear the rightmost set bit
        count += 1
    return count


if __name__ == "__main__":
    print(count_set_bits(15))  # 4
    print(count_set_bits_2(15))