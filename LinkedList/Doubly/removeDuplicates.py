class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    # Write your code here
    temp = head

    while temp and temp.next:
        if temp.data == temp.next.data:
            nxt = temp.next
            while nxt and temp.data == nxt.data:
                nxt = nxt.next
            temp.next = nxt

        temp = temp.next

    return head
