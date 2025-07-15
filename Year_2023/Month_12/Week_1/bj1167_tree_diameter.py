

def solution():
    V = int(sys.stdin.readline())
    tree = [[] for _ in range(V+1)]

    for _ in range(V):
        edges = list(map(int, sys.stdin.readline().split()))
        cur_node = edges[0]
        idx = 1
        while edges[idx] != -1:
            adj_node, adj_cost = edges[idx], edges[idx + 1]
            tree[cur_node].append((adj_node, adj_cost))
            idx += 2

    visited = [-1] * (V + 1)
    visited[1] = 0

    def dfs(node, d):
        for u, w in tree[node]:
            dist = d + w
            if visited[u] == -1:
                visited[u] = dist
                dfs(u, dist)
        return

    dfs(1, 0)
    end_node = [0, 0]
    for node, dist in enumerate(visited):
        if dist > end_node[1]:
            end_node = [node, dist]
    visited = [-1] * (V + 1)
    visited[end_node[0]] = 0
    dfs(end_node[0], 0)

    print(max(visited))
