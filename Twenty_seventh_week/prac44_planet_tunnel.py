def solution():
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    n = int(input())
    parent = [0] * (n + 1)

    edges = []
    result = 0

    for i in range(1, n + 1):
        parent[i] = i

    x = []
    y = []
    z = []

    for j in range(1, n + 1):
        data = list(map(int, input().split()))
        x.append((data[0], j))
        y.append((data[1], j))
        z.append((data[2], j))

    x.sort()
    y.sort()
    z.sort()

    for k in range(n - 1):
        edges.append((x[k + 1][0] - x[k][0], x[k][1], x[k + 1][1]))
        edges.append((y[k + 1][0] - y[k][0], y[k][1], y[k + 1][1]))
        edges.append((z[k + 1][0] - z[k][0], z[k][1], z[k + 1][1]))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(result)
    