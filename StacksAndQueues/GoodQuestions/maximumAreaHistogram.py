from collections import deque


def nearest_smaller_to_left(arr):
    stk = deque()
    res = []

    for ele in arr:
        while stk and stk[-1] >= ele:
            stk.pop()

        if not stk:
            res.append(0)

        else:
            res.append(stk[-1])

        stk.append(ele)

    return res


def nearest_smaller_to_right(arr):
    stk = deque()
    res = []

    for i in range(len(arr) - 1, -1, -1):
        ele = arr[i]

        while stk and stk[-1] >= ele:
            stk.pop()

        if not stk:
            res.append(len(arr) - 1 - i)

        else:
            res.append(stk[-1])

        stk.append(ele)
    res.reverse()
    return res


def maximum_area_histogram(heights: list) -> int:
    n = len(heights)
    left = nearest_smaller_to_left(heights)
    right = nearest_smaller_to_right(heights)
    width = [right[i] - left[i] for i in range(n)]
    area = [heights[i] * width[i] for i in range(n)]
    return max(area)


if __name__ == "__main__":
    heights = [6, 2, 5, 4, 5, 1, 6]
    print("Maximum Area of Histogram is", maximum_area_histogram(heights))
