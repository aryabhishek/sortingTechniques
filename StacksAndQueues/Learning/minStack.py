class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val, val))
            return

        min_now = self.stk[-1][1]
        self.stk.append((val, min(val, min_now)))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]


if __name__ == "__main__":
    stk = MinStack()
    print(
        stk.push(-2),
        stk.push(0),
        stk.push(-3),
        stk.getMin(),
        stk.pop(),
        stk.top(),
        stk.getMin(),
    )
