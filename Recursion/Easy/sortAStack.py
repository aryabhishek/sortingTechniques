from collections import deque


def insert(stk: deque, item: int) -> None:
    if len(stk) == 0 or stk[-1] <= item:
        stk.append(item)
        return

    last_ele = stk.pop()

    insert(stk, item)
    stk.append(last_ele)


def sort_stack(stk: deque[int]) -> None:
    if len(stk) <= 1:
        return

    last_ele = stk.pop()

    sort_stack(stk)
    insert(stk, last_ele)


if __name__ == "__main__":
    stack = deque([5, 6, 4, 3, 2, 1])

    sort_stack(stack)
    print(*stack)
