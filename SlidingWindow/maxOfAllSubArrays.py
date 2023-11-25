from collections import deque


def solve(arr, k) -> list[int]:
    n = len(arr)
    ans = []
    if k > n:
        return ans + [max(arr)] * n
    
    i, j = 0, 0
    q_max = deque()

    while j < n:
        while q_max and arr[j] > q_max[0]:
            q_max.pop()
        q_max.append(arr[j])

        if j - i + 1 == k:
            ans.append(q_max[0])
            if q_max[0] == arr[i]:
                q_max.popleft()
            i += 1

        j += 1

    return ans


if __name__ == "__main__":
    a = [1, 3, -1, -3, 5, 3, 6, 7]
    print(solve(a, 3))
