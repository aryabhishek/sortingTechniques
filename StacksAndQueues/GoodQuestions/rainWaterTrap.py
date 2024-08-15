def trap(arr: list[int]) -> int:
    n = len(arr)
    mxl = [arr[0]] * n
    mxr = [arr[-1]] * n

    for i in range(1, n):
        mxl[i] = max(mxl[i - 1], arr[i])

    for i in range(n - 2, -1, -1):
        mxr[i] = max(mxr[i + 1], arr[i])

    water = [min(mxl[i], mxr[i]) - arr[i] for i in range(n)]

    return sum(water)


class Solution:  # O(n)
    def trap(self, arr: list[int]) -> int:
        n = len(arr)
        left_max = right_max = total = 0
        l, r = 0, n - 1

        while l < r:
            if arr[l] <= arr[r]:
                if left_max > arr[l]:
                    total += left_max - arr[l]
                else:
                    left_max = arr[l]
                l += 1
            else:
                if right_max > arr[r]:
                    total += right_max - arr[r]
                else:
                    right_max = arr[r]
                r -= 1

        return total


if __name__ == "__main__":
    height = [4, 2, 0, 3, 2, 5]

    print(trap(height))
    print(Solution().trap(height))
