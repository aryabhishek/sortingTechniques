"""
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
"""

from collections import defaultdict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        adj = defaultdict(list)

        for i in range(n):
            u, v = s1[i], s2[i]
            adj[u].append(v)
            adj[v].append(u)

        res = ""
        for char in baseStr:
            vis = [0] * 26
            min_char = self.findMinChar(char, adj, vis)
            res += min_char

        return res

    def findMinChar(self, char, adj, vis):
        vis[ord(char) - 97] = 1
        ans = char

        for nei in adj[char]:
            if not vis[ord(nei) - 97]:
                ans = min(ans, self.findMinChar(nei, adj, vis))
        return ans
