"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for c1, c2 in zip(s, t):
            if (c1 in s_map and c2 != s_map[c1]) or (c2 in t_map and c1 != t_map[c2]):
                return False
            s_map[c1] = c2
            t_map[c2] = c1
        return True
