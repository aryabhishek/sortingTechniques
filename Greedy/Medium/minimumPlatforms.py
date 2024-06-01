class Solution:
    def minimumPlatform(self, n, arr, dep):
        ans, count = 0, 0
        i, j = 0, 0

        arr.sort()
        dep.sort()

        while i < n:
            if arr[i] <= dep[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            ans = max(count, ans)

        return ans
