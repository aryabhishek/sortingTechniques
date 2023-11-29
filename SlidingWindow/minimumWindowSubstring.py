def solve(s1: str, s2: str) -> int:
    n = len(s1)

    req = {}
    a_len = float("inf")
    ans = ""

    for char in s2:
        req[char] = req.get(char, 0) + 1

    count = len(req)
    i, j = 0, 0

    while j < n:
        if s1[j] in req:
            req[s1[j]] -= 1
            if req[s1[j]] == 0:
                count -= 1

        while count == 0:
            if j - i + 1 < a_len:
                ans = s1[i : j + 1]
                a_len = j - i + 1

            if s1[i] in req:
                req[s1[i]] += 1
                if req[s1[i]] > 0:
                    count += 1

            i += 1

        j += 1

    return ans


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"

    print(solve(s, t))