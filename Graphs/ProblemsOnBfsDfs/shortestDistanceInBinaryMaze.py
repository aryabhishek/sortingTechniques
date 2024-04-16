from typing import List
from collections import deque

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        n = len(grid)
        m = len(grid[0])
        dist = [[float('inf')] * m for _ in range(n)]
        
        dist[source[0]][source[1]] = 0
        
        # [dis, [x, y]] -> items of queue
        q = deque([[0, source]])
        drow = [0, 0, 1, -1]
        dcol = [1, -1, 0, 0]
        
        while q:
            dis, node = q.popleft()
            x, y = node
            
            for i in range(4):
                nrow = x + drow[i]
                ncol = y + dcol[i]
                
                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1 and dis + 1 < dist[nrow][ncol]:
                    dist[nrow][ncol] = dis + 1
                    if [nrow, ncol] == destination:
                        return dis + 1
                    q.append([dis+1, [nrow, ncol]])
                    
        return -1