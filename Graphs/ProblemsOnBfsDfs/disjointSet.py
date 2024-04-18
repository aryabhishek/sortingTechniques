class DisjointSet:

    def __init__(self, n) -> None:
        self.rank = []
        self.size = []
        self.parent = []

        for i in range(n + 1):
            self.rank.append(0)
            self.size.append(1)
            self.parent.append(i)

    def find_ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        ult_par_u = self.find_ultimate_parent(u)
        ult_par_v = self.find_ultimate_parent(v)
        if ult_par_u == ult_par_v:
            return
        if self.rank[ult_par_u] < self.rank[ult_par_v]:
            self.parent[ult_par_u] = ult_par_v
        elif self.rank[ult_par_u] > self.rank[ult_par_v]:
            self.parent[ult_par_v] = ult_par_u
        else:
            self.parent[ult_par_u] = ult_par_v
            self.rank[ult_par_v] += 1

    def union_by_size(self, u, v):
        ult_par_u = self.find_ultimate_parent(u)
        ult_par_v = self.find_ultimate_parent(v)
        if ult_par_u == ult_par_v:
            return
        if self.size[ult_par_u] < self.size[ult_par_v]:
            self.parent[ult_par_u] = ult_par_v
            self.size[ult_par_v] += self.size[ult_par_u]
        else:
            self.parent[ult_par_v] = ult_par_u
            self.size[ult_par_u] += self.size[ult_par_v]


if __name__ == "__main__":

    def is_same_component(a, b):
        if ds.find_ultimate_parent(a) == ds.find_ultimate_parent(b):
            print("Same")
        else:
            print("Not same")

    ds = DisjointSet(7)
    ds.union_by_rank(1, 2)
    ds.union_by_rank(2, 3)
    ds.union_by_rank(4, 5)
    ds.union_by_rank(6, 7)
    ds.union_by_rank(5, 6)
    is_same_component(3, 7)
    ds.union_by_rank(3, 7)
    is_same_component(3, 7)
