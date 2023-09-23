class MyQueue: # Using two stacks

    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        

    def push(self, x: int) -> None:
        while not self.is_empty():
            self.stk2.append(self.pop())

        self.stk1.append(x)

        while not len(self.stk2) == 0:
            self.stk1.append(self.stk2.pop())

    def pop(self) -> int:
        return self.stk1.pop()

    def peek(self) -> int:
        return self.stk1[-1]

    def is_empty(self) -> bool:
        return len(self.stk1) == 0
    

if __name__ == "__main__":
    q = MyQueue()
    q.push(5)
    q.push(4)
    q.push(3)
    q.push(2)
    print(q.peek())
    print(q.pop())
    print(q.is_empty())
    print(q.peek())

