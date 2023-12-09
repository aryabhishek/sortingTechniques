class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def reverse_list_iterative(head: ListNode) -> ListNode: # iterative
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt

    return prev


def reverseList(self, head: ListNode, prev=None) -> ListNode: # recursive
    if not head:
        return prev
    nxt = head.next
    head.next = prev
    return self.reverseList(nxt, head)
