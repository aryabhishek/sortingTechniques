"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Link: https://leetcode.com/problems/add-two-numbers
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        d_head = ListNode(-1)
        cur = d_head
        t1 = l1
        t2 = l2
        carry = 0
        while t1 or t2:
            summ = carry
            if t1:
                summ += t1.val
            if t2:
                summ += t2.val
            new_node = ListNode(summ % 10)
            carry = summ // 10

            cur.next = new_node
            cur = cur.next

            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next

        if carry:
            new_node = ListNode(carry)
            cur.next = new_node

        return d_head.next
