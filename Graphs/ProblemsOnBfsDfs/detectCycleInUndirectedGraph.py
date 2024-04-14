def create_adjacency_list(V, edges):
    adjacency_list = {i: [] for i in range(V)}

    for edge in edges:
        a, b = edge
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    return adjacency_list


def detect_cycle(start, adj, vis):  # bfs
    vis[start] = 1
    q = deque([(start, -1)])

    while q:
        node, parent = q.popleft()

        for adj_node in adj[node]:
            if not vis[adj_node]:
                vis[adj_node] = 1
                # node became the parent of adj_node
                q.append((adj_node, node))

            elif parent != adj_node:
                return True

    return False


def dfs(start, parent, adj, vis):
    vis[start] = 1

    for adj_node in adj[start]:
        if not vis[adj_node]:
            if dfs(adj_node, start, adj, vis):
                return True
        elif parent != adj_node:
            return True
    return False


def main():
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        a, b = map(int, input().split())
        edges.append((a, b))

    adj_list = create_adjacency_list(V, edges)
    visited = [0 for i in range(V)]

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1, adj_list, visited):
                return print("True")
    print("False")


if __name__ == "__main__":
    main()
