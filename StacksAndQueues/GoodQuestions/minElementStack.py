from collections import deque


class MinElementStack: # O(n) space
    def __init__(self) -> None:
        self.stk = deque()
        self.sup_stk = deque()

    def push(self, ele):
        self.stk.append(ele)
        if not self.sup_stk or self.sup_stk[-1] >= ele:
            self.sup_stk.append(ele)

    def pop(self):
        if not self.stk:
            return -1

        if self.sup_stk[-1] == self.stk.pop():
            self.sup_stk.pop()

    def get_min(self):
        return self.stk[0] if self.stk else float("inf")


class MinStack: # My solution O(1) space

    def __init__(self):
        self.stk = deque()

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val,val))
            return

        min_now = self.stk[-1][1]
        self.stk.append((val, min(val,min_now)))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]