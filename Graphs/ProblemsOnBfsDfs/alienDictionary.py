from collections import deque


class Solution:

    def genTopoOrder(self, V, adj):
        indeg = [0 for i in range(V)]
        ans = []

        for i in range(V):
            for node in adj[i]:
                indeg[node] += 1

        q = deque()

        for i in range(V):
            if indeg[i] == 0:
                q.append(i)

        while q:
            node = q[0]
            ans.append(q.popleft())

            for adj_node in adj[node]:
                indeg[adj_node] -= 1
                if indeg[adj_node] == 0:
                    q.append(adj_node)

        return ans

    def findOrder(self, alien_dict, N, K):
        adj = [[] for i in range(K)]

        for i in range(N - 1):
            s1 = alien_dict[i]
            s2 = alien_dict[i + 1]

            for i in range(min(len(s1), len(s2))):
                if s1[i] != s2[i]:
                    # ascii of a is 97
                    adj[ord(s1[i]) - 97].append(ord(s2[i]) - 97)
                    break

        topo = self.genTopoOrder(K, adj)
        ans = ""

        for item in topo:
            ans += chr(item + 97)

        return ans
