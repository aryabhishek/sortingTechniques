def solution(matrix):
    n = len(matrix)
    m = len(matrix[0])

    left = 0
    right = m - 1
    top = 0
    bottom = n - 1
    ans = []

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            ans.append(matrix[top][i])

        top += 1

        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])

        right -= 1
        
        if top <= bottom:
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])

            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top -1, -1):
                ans.append(matrix[i][left])

            left += 1

    return ans


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5 ],
        [14,15,16,17,6],
        [13,20,19,18,7],
        [12,11,10, 9,8]
    ]

    print(solution(matrix))

