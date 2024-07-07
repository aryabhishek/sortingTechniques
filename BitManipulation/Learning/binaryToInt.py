def binaryToInt(num: str) -> int:
    """Converts a binary number to an integer."""
    n = len(num)
    ans = 0
    p2 = 1

    for i in range(n-1, -1, -1):
        if num[i] == '1':
            ans += p2
        p2 *= 2
    return ans


if __name__ == "__main__":
    print(binaryToInt("1101"))