"""
Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string X.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

https://leetcode.com/problems/similar-string-groups
"""

from collections import defaultdict
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        self.adj = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if self.is_similar(strs[i], strs[j]):
                    self.adj[strs[i]].append(strs[j])
                    self.adj[strs[j]].append(strs[i])

        self.vis = set()
        count = 0

        for s in strs:
            if s not in self.vis:
                self.dfs(s)
                count += 1

        return count

    def is_similar(self, a, b) -> bool:
        diff = sum(1 for x, y in zip(a, b) if x != y)
        return diff == 2 or diff == 0

    def dfs(self, node):
        self.vis.add(node)

        for adj_node in self.adj[node]:
            if adj_node not in self.vis:
                self.dfs(adj_node)
