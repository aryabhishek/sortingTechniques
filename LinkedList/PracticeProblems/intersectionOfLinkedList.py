class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    address = set()
    cur = headA

    while cur:
        address.add(cur)
        cur = cur.next

    cur = headB

    while cur:
        if cur in address:
            return cur
        cur = cur.next

    return None


def alternative(headA: ListNode, headB: ListNode) -> ListNode:
    t1, t2 = headA, headB

    while t1 != t2:
        t1 = t1.next
        t2 = t2.next

        if t1 == t2:
            return t1

        if not t1:
            t1 = headB
        if not t2:
            t2 = headA

    return t1