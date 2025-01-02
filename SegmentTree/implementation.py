# range sum problem
from math import ceil, log2


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (2 * self.n)
        self.build_tree(0, 0, self.n - 1)

    def build_tree(self, idx, left, right):
        if left == right:
            self.tree[idx] = self.nums[left]
        else:
            mid = left + (right - left) // 2
            self.build_tree(2 * idx + 1, left, mid)
            self.build_tree(2 * idx + 2, mid + 1, right)
            self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2 * idx + 2]

    def __repr__(self):
        if not self.tree:
            return ""

        result = ""
        max_depth = ceil(log2(len(self.nums))) + 1
        width = 2**max_depth

        current_level = [0]
        while current_level:
            next_level = []
            level_str = ""

            for idx in current_level:
                if idx < len(self.tree) and self.tree[idx] != 0:
                    level_str += f"{str(self.tree[idx]).center(width)}"
                    next_level.append(2 * idx + 1)
                    next_level.append(2 * idx + 2)
                else:
                    level_str += " " * width
                    next_level.append(-1)
                    next_level.append(-1)

            if any(idx != -1 for idx in next_level):
                result += level_str + "\n"
            current_level = [idx for idx in next_level if idx != -1]

            width //= 2

        return result


st = SegmentTree([3, 2, 7, 1, 8, 4, 2, 6, 7, 2, 8, 9, 3, 4, 5, 20])
print(st)
