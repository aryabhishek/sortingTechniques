class MyStack: # with one queue

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.top())
            self.pop()

    def pop(self) -> int:
        return self.q.pop(0)

    def top(self) -> int:
        return self.q[0]

    def is_empty(self) -> bool:
        return len(self.q) == 0
    
class Stack2:

    def __init__(self) -> None:
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q2.append(x)
        while not self.is_empty():
            self.q2.append(self.pop())

        while not len(self.q2) == 0:
            self.q1.append(self.q2.pop(0))

    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def is_empty(self) -> bool:
        return len(self.q1) == 0
    

if __name__ == "__main__":
    stk1 = MyStack()
    stk1.push(5)
    stk1.push(4)
    stk1.push(3)
    print(stk1.top())
    print(stk1.is_empty())
    stk1.pop()
    print(stk1.top())

    stk2 = Stack2()
    stk2.push(5)
    stk2.push(4)
    stk2.push(3)
    print(stk2.top())
    print(stk2.is_empty())
    stk2.pop()
    print(stk2.top())

