def get_adj_list(num_of_nodes: int, edges: list[list[int]]) -> list[list[int]]: # For undirected graph
    ans = [[] for i in range(num_of_nodes+1)]

    for u, v in edges:
        ans[u].append(v) # The connection is bidirectional
        ans[v].append(u)

    return ans


def get_adj(n: int, edges: list[list[int]]) -> list[list[int]]: # For directed graph
    ans = [[] for i in range(n+1)]

    for u,v in edges:
        ans[u].append(v) # The connection is unidirectional

    return ans

if __name__ == "__main__":
    V = 5
    edges = [(5, 4), (2, 3), (4, 1), (4, 0), (2, 1)]

    print(get_adj_list(V, edges=edges))
    print(get_adj(V, edges))
