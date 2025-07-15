from collections import deque

def solution(N,M,Field):
    n, m = N,M

    field = Field

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if field[nx][ny] == 0:
                    continue
                if field[nx][ny] == 1:
                    field[nx][ny] = field[x][y] + 1
                    queue.append((nx, ny))
        return field[n - 1][m - 1]

    return bfs(0,0)