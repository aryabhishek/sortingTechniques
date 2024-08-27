"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

https://leetcode.com/problems/path-with-maximum-probability
"""

import heapq
from math import log, exp
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            log_prob = log(succProb[i])
            adj[u].append((v, log_prob))
            adj[v].append((u, log_prob))

        return self.dijkstra(n, adj, start_node, end_node)

    def dijkstra(
        self, n: int, adj: List[List[tuple]], start_node: int, end_node: int
    ) -> float:
        dist = [float("-inf")] * n
        dist[start_node] = 0
        max_heap = [(-0, start_node)]

        while max_heap:
            neg_dis, node = heapq.heappop(max_heap)
            dis = -neg_dis

            if node == end_node:
                return exp(dis)

            if dis < dist[node]:
                continue

            for adj_node, wt in adj[node]:
                new_dis = dis + wt
                if new_dis > dist[adj_node]:
                    dist[adj_node] = new_dis
                    heapq.heappush(max_heap, (-new_dis, adj_node))

        return 0.0
