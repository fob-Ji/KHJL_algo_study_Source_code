from collections import deque


def solution():
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited_dfs = [False] * (n + 1)
    visited_bfs = [False] * (n + 1)
    for _ in range(m):
        src, dst = map(int, input().split())
        graph[src].append(dst)

    def dfs(start):
        visited_dfs[start] = True
        print(start, end=' ')
        for adj in graph[start]:
            if not visited_dfs[adj]:
                dfs(adj)

    def bfs(start):
        q = deque()
        q.append(start)
        visited_bfs[start] = True

        while q:
            s = q.popleft()
            print(s, end=" ")

            for adj in graph[s]:
                if not visited_bfs[adj]:
                    q.append(adj)
                    visited_bfs[adj] = True

    dfs(v)
    print()
    bfs(v)

