"""
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

https://leetcode.com/problems/satisfiability-of-equality-equations/
"""

from typing import List


class DisjointSet:

    def __init__(self, n) -> None:
        self.rank = []
        self.parent = []

        for i in range(n + 1):
            self.rank.append(0)
            self.parent.append(i)

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        ult_par_u = self.find(u)
        ult_par_v = self.find(v)
        if ult_par_u == ult_par_v:
            return
        if self.rank[ult_par_u] < self.rank[ult_par_v]:
            self.parent[ult_par_u] = ult_par_v
        elif self.rank[ult_par_u] > self.rank[ult_par_v]:
            self.parent[ult_par_v] = ult_par_u
        else:
            self.parent[ult_par_u] = ult_par_v
            self.rank[ult_par_v] += 1


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ds = DisjointSet(26)

        for eq in equations:
            if eq[1] == "=":
                u, v = ord(eq[0]) - 97, ord(eq[-1]) - 97
                ds.union(u, v)

        for eq in equations:
            if eq[1] == "!":
                u, v = ord(eq[0]) - 97, ord(eq[-1]) - 97
                if ds.find(u) == ds.find(v):
                    return False

        return True
