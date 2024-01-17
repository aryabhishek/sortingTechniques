"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
Link: https://leetcode.com/problems/reverse-linked-list-ii/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        prev = None
        cur = head

        for i in range(1, left):
            prev = cur
            cur = cur.next

        start = prev
        s2 = cur
        nxt = cur.next

        for i in range(right - left):
            cur.next = prev
            prev = cur
            cur = cur.next
            nxt = cur.next

        start.next = prev
        s2.next = cur

        return head
