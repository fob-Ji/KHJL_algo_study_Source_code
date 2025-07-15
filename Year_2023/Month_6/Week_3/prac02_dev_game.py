def solution():
    n, m = map(int, input().split())

    visited = [[0] * m for _ in range(n)]

    x, y, direction = map(int, input().split())
    visited[x][y] = 1

    field = []
    for i in range(n):
        field.append(list(map(int, input().split())))

    # 문제에서 북,동,남,서 순으로 정의
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3

    count = 1
    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 정면에 아직 가지 않은 칸이 존재하며 육지인 경우 이동
        if d[nx][ny] == 0 and field[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        #회전하고 정면에 가지 않은 칸이 없거나 바다일 때
        else:
            #4방향을 다 돌았는지 간단하게 확인하기 위한 변수
            turn_time += 1

            if turn_time == 4:
                nx = x - dx[direction]
                ny = y - dy[direction]
                #뒤로 갈 수 있으면
                if field[nx][ny] == 0 :
                    x = nx
                    y = ny
                else:
                    break
                #뒤로 갔으면 회전 수를 초기화
                turn_time = 0

    print(count)