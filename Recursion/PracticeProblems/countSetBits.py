def count_set_bits(s: str, count: int) -> int:
    if not s:
        return count

    if s[-1] == "1":
        count += 1

    return count_set_bits(s[:-1], count)


def alternative(s: str, idx: int = 0, count: int = 0) -> int:
    if idx == len(s):
        return count
    
    if s[idx] == "1":
        count += 1

    return alternative(s, idx + 1, count)


if __name__ == "__main__":
    string = "11101101111111011111101111111101" # set bit means 1

    print(count_set_bits(string, 0))
    print(alternative(string, 0, 0))
