"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
"""

from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_set = set(bank)

        q = deque([startGene])
        vis = set([startGene])
        level = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endGene:
                    return level

                for char in "ACGT":
                    for i in range(8):
                        nxt = cur[0:i] + char + cur[i + 1 :]
                        if nxt not in vis and nxt in bank_set:
                            vis.add(nxt)
                            q.append(nxt)
            level += 1
        return -1
