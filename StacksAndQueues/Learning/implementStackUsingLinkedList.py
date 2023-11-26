class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, value) -> None:
        if self.head is None:
            self.head = Node(value)
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = Node(value)
        self.tail = cur.next

    def popright(self) -> int:
        if not self.head:
            return float("inf")

        prev = None
        cur = self.head

        while cur.next:
            prev = cur
            cur = cur.next

        if prev:
            ans = cur.val
            self.tail = prev
            prev.next = None
        else:
            ans = self.head.val
            self.head = None
            self.tail = None

        return ans

    def _display(self, node: Node):
        if node is None:
            return

        print(node.val)
        node = node.next
        self._display(node)

    def display(self) -> None:
        self._display(self.head)


class Stack:
    def __init__(self) -> None:
        self.ll = LinkedList()

    def push(self, item) -> None:
        self.ll.append(item)

    def pop(self) -> int:
        return self.ll.popright()

    def peek(self):
        if self.ll.tail:
            print(self.ll.tail.val)
        else:
            print("The Stack is Empty")

    def display(self) -> None:
        self.ll.display()


if __name__ == "__main__":
    stk = Stack()

    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.push(4)
    stk.push(5)

    for i in range(5):
        stk.peek()
        print(stk.pop())
