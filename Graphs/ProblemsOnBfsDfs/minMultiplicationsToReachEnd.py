from typing import List
from collections import deque
import sys


class Solution:

    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        # code here
        if start == end:
            return 0
        q = deque()
        #        node, steps
        q.append([start, 0])

        dist = [sys.maxsize for i in range(100000)]
        dist[start] = 0
        mod = 100000
        while q:
            node, steps = q.popleft()

            for i in arr:
                num = (i * node) % mod
                if steps + 1 < dist[num]:
                    dist[num] = steps + 1
                    if num == end:
                        return steps + 1
                    q.append([num, steps + 1])

        return -1
