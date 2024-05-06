class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        def compare(s1, s2):
            if len(s1) != len(s2) + 1:
                return False

            first = 0
            second = 0

            while first < len(s1):
                if second < len(s2) and s1[first] == s2[second]:
                    first += 1
                    second += 1
                else:
                    first += 1

            return first == len(s1) and second == len(s2)

        n = len(words)
        words.sort(key=len)

        dp = [1] * n
        mx = 0

        for i in range(n):
            for prev in range(i):
                if compare(words[i], words[prev]) and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
            if mx < dp[i]:
                mx = dp[i]

        return mx
