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