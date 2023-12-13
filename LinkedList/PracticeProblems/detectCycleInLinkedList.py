class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def dectect_cycle(head: ListNode) -> bool:
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False
