"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        items = []
        while cur:
            items.append(cur.val)
            cur = cur.next
        items.sort()
        i = 0
        cur = head
        while cur:
            cur.val = items[i]
            cur = cur.next
            i += 1

        return head
