class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def detectCycle(self, head: ListNode) -> ListNode:
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None
