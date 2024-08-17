"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

https://leetcode.com/problems/time-needed-to-inform-all-employees/
"""


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: list[int], informTime: list[int]
    ) -> int:
        self.time = 0
        self.adj = [[] for _ in range(n)]
        self.inform = informTime

        for i in range(n):
            emp = i
            boss = manager[i]
            if boss != -1:
                self.adj[boss].append(emp)

        self.dfs(headID, 0)
        return self.time

    def dfs(self, start, cur_time):
        self.time = max(self.time, cur_time)

        for emp in self.adj[start]:
            self.dfs(emp, cur_time + self.inform[start])
