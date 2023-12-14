class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def deleteAllOccurrences(head: Node, k: int) -> Node:
    # Write your code here
    cur = head

    while cur:
        if cur.data == k:
            if cur == head:
                head = cur.next

            next_node = cur.next
            prev_node = cur.prev

            if prev_node:
                prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node

        cur = cur.next

    return head
