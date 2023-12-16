class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        temp, next_node, prev_node = head, None, None

        while temp:
            kth_node = self.getKthNode(temp, k)
            if not kth_node:
                if prev_node:
                    prev_node.next = temp
                break

            next_node = kth_node.next
            kth_node.next = None
            self.reverseLL(temp)
            if temp == head:
                head = kth_node
            else:
                prev_node.next = kth_node

            prev_node = temp
            temp = next_node

        return head

    def reverseLL(self, head: ListNode, prev=None) -> ListNode:
        if not head:
            return prev

        nxt = head.next
        head.next = prev
        return self.reverseLL(nxt, head)

    def getKthNode(self, head: ListNode, k: int) -> ListNode:
        temp = head
        k -= 1
        while temp and k > 0:
            k -= 1
            temp = temp.next

        return temp
