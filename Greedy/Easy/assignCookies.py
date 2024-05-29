class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        m, n = len(g), len(s)
        l, r = 0, 0

        while l < m and r < n:
            if g[l] <= s[r]:
                l += 1
            r += 1

        return l
