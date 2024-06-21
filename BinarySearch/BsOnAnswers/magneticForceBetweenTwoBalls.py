"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.
"""


class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        def can_place(force, arr, balls):
            count = 1
            prev = arr[0]

            for i in range(1, len(arr)):
                cur = arr[i]
                if cur - prev >= force:
                    count += 1
                    prev = cur

                if count >= m:
                    return True

            return False

        position.sort()
        left = 1
        right = (position[-1] - position[0]) // (m - 1)

        while left <= right:
            min_force = left + (right - left) // 2

            if can_place(min_force, position, m):
                left = min_force + 1
            else:
                right = min_force - 1
        return right
