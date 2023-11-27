def solve(string: str, k: int) -> int:
    unique = {}

    n = len(string)
    i, j = 0, 0
    ans = 0

    while j < n:
        unique[string[j]] = unique.get(string[j], 0) + 1

        if len(unique) < k:
            j += 1

        elif len(unique) == k:
            ans = max(ans, j - i + 1)
            j += 1

        else:
            while len(unique) > k:
                unique[string[i]] -= 1
                if unique[string[i]] == 0:
                    del unique[string[i]]
                i += 1
            j += 1

    return ans


if __name__ == "__main__":
    string = "aabacbebebe"
    k = 3
    print(solve(string, k))