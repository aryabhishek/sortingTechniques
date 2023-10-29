from collections import deque


def nearest_smaller_to_right(arr):
    stk = deque()
    res = []

    for i in range(len(arr)-1, -1, -1):
        ele = arr[i]

        while stk and stk[-1] >= ele:
            stk.pop()

        if not stk:
            res.append(-1)

        else:
            res.append(stk[-1])

        stk.append(ele)
    res.reverse()
    return res


if __name__ == "__main__":
    arr = [50, 30, 40, 80, 70, 60, 20]

    print(nearest_smaller_to_right(arr))