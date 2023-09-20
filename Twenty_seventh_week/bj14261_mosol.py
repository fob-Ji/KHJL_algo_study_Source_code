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

    n, m = map(int, input().split())
    genders = list(input().split())
    parent = []

    edges = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        edges.append((d, u, v))

    edges.sort()
    result, paths = 0, 0

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b) and genders[a - 1] != genders[b - 1]:
            union_parent(parent, a, b)
            result += cost
            paths += 1

    if paths == n - 1:
        print(result)
    else:
        print(-1)
