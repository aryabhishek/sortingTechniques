from collections import deque


def insert(stk: deque, item: int) -> None:
    if not stk:
        stk.append(item)
        return

    top = stk.pop()

    insert(stk, item)
    stk.append(top)


def reverse(stk: deque) -> None:
    if len(stk) == 1:
        return

    top = stk.pop()

    reverse(stk)
    insert(stk, top)


if __name__ == "__main__":
    stack = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    reverse(stack)

    print(*stack)
