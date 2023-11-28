def solve(toys: str, allowed: int) -> int:
    n = len(toys)
    i, j = 0, 0
    ans = 0
    r_count = 0
    types = {}

    while j < n:
        types[toys[j]] = types.get(toys[j], 0) + 1
        r_count += 1
        if len(types) < allowed:
            j += 1

        elif len(types) == allowed:
            ans = max(ans, r_count)
            j += 1

        else:
            while len(types) > allowed:
                types[toys[i]] -= 1
                r_count -= 1
                if types[toys[i]] == 0:
                    del types[toys[i]]
                i += 1
            j += 1

    return ans


if __name__ == "__main__":
    t = "aabacaccbcca"
    a = 2
    print(solve(t, a))
