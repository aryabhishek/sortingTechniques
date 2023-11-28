def solve(string: str) -> int:
    unique = {}

    n = len(string)
    i, j = 0, 0
    ans = 0

    while j < n:
        unique[string[j]] = unique.get(string[j], 0) + 1

        if len(unique) == j - i + 1:
            ans = max(ans, j - i + 1)
            j += 1

        elif len(unique) < j - i + 1:
            while len(unique) < j - i + 1:
                unique[string[i]] -= 1
                if unique[string[i]] == 0:
                    del unique[string[i]]
                i += 1
            j += 1

    return ans


if __name__ == "__main__":
    s = "pwwkew"
    print(solve(s))

    s = "aabcabebebe"
    print(solve(s))
