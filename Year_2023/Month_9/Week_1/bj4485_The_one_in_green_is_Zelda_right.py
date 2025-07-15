import heapq


def solution():
    INF = int(1e9)
    count = 1
    while True:
        n = int(input())
        if n != 0:
            field = []
            for _ in range(n):
                field.append(list(map(int, input().split())))
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            dist = [[INF]*n for _ in range(n)]

            pq = []
            x, y = 0, 0
            dist[x][y] = field[x][y]
            heapq.heappush(pq, (field[x][y], x, y))

            while pq:
                value, x, y = heapq.heappop(pq)

                if dist[x][y] < value:
                    continue
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    else:
                        cost = value + field[nx][ny]
                        if cost < dist[nx][ny]:
                            dist[nx][ny] = cost
                            heapq.heappush(pq, (cost, nx, ny))
            print("Problem", end=" ")
            print(count, end=": ")
            print(dist[n-1][n-1])
            count += 1
        else:
            break
