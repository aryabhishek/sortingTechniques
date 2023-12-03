class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


def reverse_dll(head: Node) -> Node:
    cur = head
    h = None
    while cur:
        cur.next, cur.prev = cur.prev, cur.next
        h = cur
        cur = cur.prev

    return h
