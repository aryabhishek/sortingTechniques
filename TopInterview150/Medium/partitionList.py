"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Link: https://leetcode.com/problems/partition-list 
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = ListNode(-1)
        right = ListNode(-1)
        d_left = left
        d_right = right

        temp = head
        while temp:
            if temp.val < x:
                left.next = ListNode(temp.val)
                left = left.next
            else:
                right.next = ListNode(temp.val)
                right = right.next
            temp = temp.next

        left.next = d_right.next

        return d_left.next
