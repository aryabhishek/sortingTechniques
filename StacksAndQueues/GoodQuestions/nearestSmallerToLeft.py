from collections import deque


def nearest_smaller_to_left(arr):
    stk = []
    res = []

    for ele in arr:
        while stk and stk[-1] >= ele:
            stk.pop()

        if not stk:
            res.append(-1)
        
        else:
            res.append(stk[-1])

        stk.append(ele)

    return res


if __name__ == "__main__":
    arr = [5, 3, 2, 4, 6, 7, 8, 9, 10]

    print(nearest_smaller_to_left(arr))