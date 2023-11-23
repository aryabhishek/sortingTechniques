from collections import deque

def solve(arr, k):
    q = deque()

    i, j = 0, 0

    while j < len(arr):
        if arr[j] < 0:
            q.append(arr[j])

        if j == k + i - 1:
            if q:
                print(q[0])
                if arr[i] == q[0]:
                    q.popleft()
            else:
                print(0)
            i += 1

        j += 1


if __name__ == "__main__":
    a = [12, -1, -7, 8, -15, 30, 16, 28]
    solve(a, 3)