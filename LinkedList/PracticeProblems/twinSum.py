class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def naive_sol(head: ListNode) -> ListNode:
    cur = head.next
    d_head = ListNode(-1)
    ans = d_head

    while cur:
        total = 0
        while cur and cur.val != 0:
            total += cur.val
            cur = cur.next

        ans.next = ListNode(total)
        ans = ans.next
        cur = cur.next

    return d_head.next


def pairSum(head: ListNode) -> int:
    slow, fast = head, head
    ans = 0

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev, cur = None, slow

    while cur:
        cur.next, cur, prev = prev, cur.next, cur

    while prev:
        ans = max(ans, head.val + prev.val)
        prev = prev.next
        head = head.next

    return ans
