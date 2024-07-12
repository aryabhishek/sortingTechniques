"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""


class Solution:
    def sortList(self, head: object) -> object:
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
