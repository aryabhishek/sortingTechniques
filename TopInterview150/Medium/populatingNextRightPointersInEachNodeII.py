"""

"""

from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return

        q = deque([root])

        while q:
            q_len = len(q)
            prev = None

            for i in range(q_len):
                cur = q.popleft()

                if prev:
                    prev.next = cur

                prev = cur

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

        return root
