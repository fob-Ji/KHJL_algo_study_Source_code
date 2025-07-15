import sys
from collections import deque


def solution():
    M, N, H = map(int, sys.stdin.readline().split())
    boxes = []
    q = deque([])

    for i in range(H):
        box = []
        for j in range(N):
            box.append(list(map(int, sys.stdin.readline().split())))
            for k in range(M):
                if box[j][k] == 1:
                    q.append([i, j, k])
        boxes.append(box)

    dz = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, 1, -1, 0, 0]
    dy = [0, 0, 0, 0, 1, -1]

    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and boxes[nz][nx][ny] == 0:
                q.append([nz, nx, ny])
                boxes[nz][nx][ny] = boxes[z][x][y] + 1

    day = 0
    for box in boxes:
        for line in box:
            for tomato in line:
                if tomato == 0:
                    print(-1)
                    exit(0)
            day = max(day, max(line))
    print(day - 1)
