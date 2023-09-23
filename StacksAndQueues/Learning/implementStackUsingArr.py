class Stack:

    def __init__(self, capacity: int):
        # Write your code here.
        self.top_ele = 0
        self.cap = capacity
        self.arr = [0]*capacity

    def push(self, num: int) -> None:
        # Write your code here.
        if not self.isFull():
            self.arr[self.top_ele] = num
            self.top_ele += 1
        else:
            print("The Stack is full...can't add more elements")

    def pop(self) -> int:
        # Write your code here.
        if self.top_ele > 0:
            self.top_ele -= 1
            item = self.arr[self.top_ele]
            return item
        return -1

    def top(self) -> int:
        # Write your code here.
        if self.top_ele > 0:
            return self.arr[self.top_ele - 1]
        return -1

    def isEmpty(self) -> int:
        # Write your code here.
        if self.top_ele == 0:
            return 1
        return 0

    def isFull(self) -> int:
        # Write your code here.
        if self.top_ele >= self.cap:
            return 1
        return 0

    def display(self) -> None:
        print(self.arr[:self.top_ele])


if __name__ == "__main__":
    stack = Stack(5)
    print(stack.pop())
    stack.display()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.pop()
    stack.display()
    stack.push(-2)
    print(stack.top())
    stack.display()
    print(bool(stack.isFull()))
    stack.push(6)
    stack.push(8)
    print(bool(stack.isFull()))
    stack.push(9)
    stack.display()

