class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def deleteMiddle(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None

    slow, fast = head, head.next.next

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    slow.next = slow.next.next
    return head
