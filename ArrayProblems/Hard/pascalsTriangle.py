def generate_row(row):
    ans = 1

    res = [1]

    for col in range(1, row):
        ans *= row - col
        ans //= col
        res.append(ans)

    return res


def generate(n: int) -> list[list[int]]:

    ans = []

    for i in range(1, n + 1):
        ans.append(generate_row(i))

    return ans


if __name__ == "__main__":
    n = 6
    triangle = generate(n)

    for row in triangle:
        print(row)
