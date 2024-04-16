from collections import deque
import sys, heapq


class Solution:

    def MinimumEffort(self, a):
        # code here
        n = len(a)
        m = len(a[0])
        dist = [[sys.maxsize] * m for i in range(n)]
        dist[0][0] = 0
        pq = []
        heapq.heappush(pq, [0, [0, 0]])

        drow = [0, 0, 1, -1]
        dcol = [1, -1, 0, 0]

        while pq:
            diff, node = pq[0]
            x, y = node
            heapq.heappop(pq)
            if x == n - 1 and y == m - 1:
                return diff

            for i in range(4):
                nrow = x + drow[i]
                ncol = y + dcol[i]

                if 0 <= nrow < n and 0 <= ncol < m:
                    new_diff = max(abs(a[x][y] - a[nrow][ncol]), diff)
                    if new_diff < dist[nrow][ncol]:
                        dist[nrow][ncol] = new_diff
                        heapq.heappush(pq, [new_diff, [nrow, ncol]])

        return 0
