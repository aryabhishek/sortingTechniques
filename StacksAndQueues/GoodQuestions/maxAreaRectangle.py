from maximumAreaHistogram import maximum_area_histogram

def max_area_rectangle(mat: list[list[int]]) -> int:
    n, m = len(mat), len(mat[0])

    mod_mat = [mat[0]]
    for i in range(1,n):
        row = []
        for j in range(m):
            if mat[i][j] != 0:
                row.append(mat[i][j] + mod_mat[-1][j])
            else:
                row.append(0)
        mod_mat.append(row)

    ans = 0
    for i in range(len(mod_mat)):
        ans = max(ans, maximum_area_histogram(mod_mat[i]))

    return ans


if __name__ == "__main__":
    m = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]
    ]

    print(max_area_rectangle(m))