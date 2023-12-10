class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.
def helper(head: Node) -> Node:
    if not head:
        return 1
    
    carry = helper(head.next)
    head.data += carry
    if head.data < 10: return 0
    head.data = 0
    return 1

def addOne(head: Node) -> Node:
    # write your code here
    carry = helper(head)

    if carry:
        new_head = Node(1)
        new_head.next = head
        head = new_head

    return head
