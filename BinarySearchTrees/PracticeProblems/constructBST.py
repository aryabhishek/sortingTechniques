class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = 0
        self.left = None
        self.right = None


def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
    self.i = 0
    return self.build(preorder, float('inf'))


def build(self, arr, u_bound):
    if self.i == len(arr) or arr[self.i] > u_bound:
        return None

    root = TreeNode(arr[self.i])
    self.i += 1

    root.left = self.build(arr, root.val)
    root.right = self.build(arr, u_bound)

    return root
