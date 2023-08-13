from collections import deque


def del_mid_ele(stack: deque, k: int) -> None:
    if len(stack) == 0:
        return

    elif k == 1:
        stack.pop()
        return

    last_ele = stack.pop()

    del_mid_ele(stack, k-1)
    stack.append(last_ele)


if __name__ == "__main__":
    stk = deque([1, 2, 3, 4, 5])
    k = len(stk)//2 + 1

    del_mid_ele(stk, k)

    print(*stk)
