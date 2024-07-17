"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            if prev.next == cur:
                prev = prev.next
            else:
                prev.next = cur.next

            cur = cur.next

        return dummy.next
