from collections import deque


class BinaryTreeNode:

    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, node) -> None:
        self.left = node

    def insert_right(self, node) -> None:
        self.right = node

    def display(self, node):
        if node is None:
            return

        print(node.val)
        self.display(node.left)
        self.display(node.right)


bt = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2)
bt3 = BinaryTreeNode(3)
bt.insert_left(bt2)
bt.insert_right(bt3)
bt4 = BinaryTreeNode(4)
bt5 = BinaryTreeNode(None)
bt2.insert_left(bt4)
bt2.insert_right(bt5)
bt6 = BinaryTreeNode(6)
bt7 = BinaryTreeNode(7)
bt3.insert_left(bt6)
bt3.insert_right(bt7)
bt.display(bt)
