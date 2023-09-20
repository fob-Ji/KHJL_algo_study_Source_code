from collections import deque


def solution():
    n = int(input())
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for i in range(n+1)]
    data = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(input())
    for k in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for r in range(1, n + 1):
        if indegree[r] == 0:
            q.append(r)

    certain = True
    cycle = False

    for s in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)

        for t in range(1, n + 1):
            if graph[now][t]:
                indegree[t] -= 1
                if indegree[t] == 0:
                    q.append(t)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()

