class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def naive_sol(head: ListNode) -> ListNode:
    arr = []
    cur = head

    while cur:
        arr.append(cur.val)
        cur = cur.next

    l, r = 0, len(arr)-1
    
    ans = float('-inf')
    while l < r:
        ans = max(ans, arr[l]+arr[r])
        l += 1
        r -= 1
    
    return ans

def mergeNodes(head: ListNode) -> ListNode:
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
