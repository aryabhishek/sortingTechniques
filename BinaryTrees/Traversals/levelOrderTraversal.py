from collections import deque
from PracticeProblems.binaryTree import BinaryTreeNode


def level_order(root: BinaryTreeNode) -> list[list[int]]:
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
