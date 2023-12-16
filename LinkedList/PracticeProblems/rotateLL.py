class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        tail = head
        n = 1
        while tail.next:
            n += 1
            tail = tail.next

        if k % n == 0:
            return head

        k %= n

        tail.next = head
        newLastNode = self.findKthNode(head, n - k)
        head = newLastNode.next
        newLastNode.next = None

        return head

    def findKthNode(self, head, k):
        temp = head
        count = 1
        while temp:
            if count == k:
                return temp
            k -= 1
            temp = temp.next
        return temp
