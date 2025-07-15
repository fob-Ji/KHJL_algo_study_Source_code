from collections import deque
def solution(): #n,k,apples,l,directions
    n = int(input())
    k = int(input())
    field = [[0] * n for _ in range(n)]

    for i in range(k):
        r, c = map(int, input().split())
        field[r - 1][c - 1] = 1

    dict = {}
    l = int(input())
    for j in range(l):
        second, way_change = input().split()
        dict[int(second)] = way_change

    q = deque()
    x = 0
    y = 0

    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direction = 0

    q.append((x, y))

    for sec in range(1, 10000):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if (nx, ny) in q:
            print(sec)
            break

        if -1 < nx < n and -1 < ny < n:
            q.append((nx, ny))
            if field[nx][ny] == 0:
                q.popleft()
            else:
                field[nx][ny] = 0
        else:
            print(sec)
            break

        if sec in dict:
            if dict[sec] == 'L':
                direction -= 1
            else:
                direction += 1
            if direction == -1:
                direction = 3
            else:
                direction %= 4
        # for i in range(l):
        #     if directions[i][0] == sec:
        #         if directions[i][1] == 'L':
        #             direction -= 1
        #         else:
        #             direction += 1
        #
        #         if direction == -1:
        #             direction = 3
        #         else:
        #             direction %= 4
        #         break
        x = nx
        y = ny
