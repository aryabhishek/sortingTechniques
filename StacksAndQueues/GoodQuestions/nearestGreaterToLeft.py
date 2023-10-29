from collections import deque


def nearest_greater_to_left(arr):
    stk = deque()
    res = []

    for ele in arr:
        while stk and stk[-1] <= ele:
            stk.pop()

        if not stk:
            res.append(-1)

        else:
            res.append(stk[-1])

        stk.append(ele)

    return res


if __name__ == "__main__":
    arr = [4, 5, 2, 7, 8, 9, 3, 6, 10]

    print(nearest_greater_to_left(arr))