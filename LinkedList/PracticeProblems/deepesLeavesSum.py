from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        return sum(self.level_order(root)[-1])

    def solve(self, root):
        if not root:
            return

        # We need only the deepest nodes so we can't just add all leaf nodes' values
        if not root.left and not root.right:
            self.ans += root.val

        self.solve(root.left)
        self.solve(root.right)

    def level_order(self, root) -> list[list[int]]:
        q = deque()

        q.append(root)
        ans = []

        while q:
            temp = []

            for _ in range(len(q)):
                node = q[0]
                q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(temp)
        return ans

    def deepestLeavesSum(self, root: TreeNode) -> int: #best solution
        t = [root]
        while t:
            p = t
            t = []
            for l in p:
                if l.right:
                    t.append(l.right)
                if l.left:
                    t.append(l.left)

        return sum([l.val for l in p])
