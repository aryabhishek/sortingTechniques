from reverseLinkedList import reverseList

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        new_head = reverseList(slow.next)
        first = head
        second = new_head

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next
        return True
