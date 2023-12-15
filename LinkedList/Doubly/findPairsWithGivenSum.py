class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

# brute force
def findPairs(head: Node, k: int) -> [[int]]:
    t1, t2 = head, head.next
    ans = []

    while t1 and t2:
        while t2:
            if t1.data + t2.data == k:
                ans.append([t1.data, t2.data])
            t2 = t2.next

        t1 = t1.next
        t2 = t1.next

    return ans

class Solution:
    def find_tail(self, head: Node) -> Node:
        cur = head
        while cur.next:
            cur = cur.next
        return cur
    
    def optimal(self, head: Node, k: int) -> [[int]]:
        if not head:
            return []

        left, right = head, self.find_tail(head)
        ans = []

        while left.data < right.data:
            if left.data + right.data == k:
                ans.append([left.data, right.data])
                left = left.next
                right = right.prev

            elif left.data + right.data < k:
                left = left.next

            else:
                right = right.prev

        return ans

