class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def append(self, value) -> None:

        if self.head is None:
            self.head = Node(value)
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = Node(value)
    
    def _display(self, node:Node):
        if node is None:
            return
        
        print(node.val)
        node = node.next
        self._display(node)

    def display(self) -> None:
        self._display(self.head)


ll = LinkedList()
ll.append(5)
ll.append(4)
ll.display()