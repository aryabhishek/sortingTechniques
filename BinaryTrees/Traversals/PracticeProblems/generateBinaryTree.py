from binaryTree import BinaryTreeNode

class GenerateBinaryTree:

    def __init__(self) -> None:
        pass

    def build(self, arr: list) -> BinaryTreeNode:
        assert arr, "The given array should not be empty"

        root = BinaryTreeNode(arr[0])
        self.rec_build(root, arr[1:])
        return root

    def rec_build(self, node: BinaryTreeNode, arr: list) -> None:
        if not arr:
            return

        if len(arr) >= 2:
            node.left = BinaryTreeNode(arr[0]) if arr[0] else None
            node.right = BinaryTreeNode(arr[1]) if arr[1] else None
            self.rec_build(node.left, arr[2:])
            self.rec_build(node.right, arr[2:])

        else:
            node.left = BinaryTreeNode(arr[0]) if arr[0] else None
            self.rec_build(node.left, arr[1:])

    def iterative(self, arr):
        root = BinaryTreeNode(arr[0])

        cur = root
        l, r = 1, 2
        flag = True
        while l < len(arr) or r < len(arr):
            if r >= len(arr):
                cur.left = BinaryTreeNode(arr[l])

            elif l >= len(arr):
                cur.right = BinaryTreeNode(arr[r])

            else:
                cur.left = BinaryTreeNode(arr[l])
                cur.right = BinaryTreeNode(arr[r])
            l += 2
            r += 2
            if flag:
                cur = cur.left
            else:
                cur = cur.right
            flag = not flag

        return root


if __name__ == "__main__":
    import os
    generator = GenerateBinaryTree()
    array = [1, 2, 3, 4, None, 6, 7]
    tree = generator.iterative(array)
    os.system("cls")
    tree.display(tree)
