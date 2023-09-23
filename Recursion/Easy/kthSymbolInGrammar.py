def kth_grammar(n: int, k: int) -> int:
    if n == 1 and k == 1:
        return 0

    mid = 2**(n-1)//2

    if k <= mid:
        return kth_grammar(n-1, k)

    else:
        return 1 if kth_grammar(n-1, k-mid) == 0 else 0


def top_leetcode_1(n: int, k: int) -> int:
    return bin(k-1).count("1") % 2


def top_leetcode_2(n: int, k: int) -> int:
    if n == 1:
        return 0

    return (1-k % 2) ^ top_leetcode_2(n-1, (k+1)//2)


if __name__ == "__main__":
    n = 7
    k = 4

    print(kth_grammar(n, k))
    print(top_leetcode_1(n, k))
    print(top_leetcode_2(n, k))
