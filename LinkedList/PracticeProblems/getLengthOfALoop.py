class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.
def getLen(slow, fast):
    count = 0
    while slow and fast:
        slow = slow.next
        count += 1
        if slow == fast:
            return count
    return 0


def lengthOfLoop(head: Node) -> int:
    # Write your code here
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return getLen(slow, fast)

    return 0
