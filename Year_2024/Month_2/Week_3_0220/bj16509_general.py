from collections import deque


def solution():
    visit = [[0] * 9 for _ in range(10)]
    r, c = map(int, input().split())
    a, b = map(int, input().split())

    def valid(i, j, dt):
        dx = [
            [-1, -2],
            [-1, -2],
            [0, -1],
            [0, -1],
            [0, 1],
            [0, 1],
            [1, 2],
            [1, 2]
        ]
        dy = [
            [0, -1],
            [0, 1],
            [-1, -2],
            [1, 2],
            [-1, -2],
            [1, 2],
            [0, -1],
            [0, 1]
        ]
        for k in range(2):
            x, y = i + dx[dt][k], j + dy[dt][k]
            if x == a and y == b:
                return 0
        return 1

    def bfs(i, j):
        q = deque()
        visit[i][j] = 1
        q.append((i, j, 0))
        dx = [-3, -3, -2, -2, 2, 2, 3, 3]
        dy = [-2, 2, -3, 3, -3, 3, -2, 2]

        while q:
            i, j, c = q.popleft()
            for k in range(8):
                x, y = i + dx[k], j + dy[k]
                if not (0 <= x < 10 and 0 <= y < 9): continue
                if not valid(i, j, k): continue
                if visit[x][y]: continue
                if x == a and y == b: return c + 1
                visit[x][y] = 1
                q.append((x, y, c + 1))
        return -1

    print(bfs(r, c))
