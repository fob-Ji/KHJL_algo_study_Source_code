import copy
from collections import deque

def solution(land):
    answer = 0
    n, m = len(land), len(land[0])

    ''' 
    정확성 테스트만 통과
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for j in range(m):
        visited = [[0] * m for _ in range(n)]
        oil = 0
        for i in range(n):
            if land[i][j] == 1 and visited[i][j] == 0:
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    oil += 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and visited[nx][ny] == 0:
                                q.append((nx,ny))
                                visited[nx][ny] = 1
        answer = oil if answer < oil else answer
    '''
    visited = [[0]*m for _ in range(n)]
    field = [[0]*m for _ in range(n)]
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    olis = [0]*(n*m)
    olis_num = 0

    #석유 번호와 갯수 저장
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                if land[i][j] == 1:
                    olis_num += 1
                    q.append((i, j))
                    visited[i][j] = 1
                    field[i][j] = olis_num
                    while q:
                        x, y = q.popleft()
                        olis[olis_num] += 1
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < n and 0 <= ny <m:
                                if land[nx][ny] == 1 and visited[nx][ny] == 0:
                                    q.append((nx, ny))
                                    visited[nx][ny] = 1
                                    field[nx][ny] = olis_num
                else:
                    visited[i][j] = 1

    #해당 열을 시추하면 몇번 석유들을 추출할 수 있는지 확인
    drill = [[] for _ in range(m)]
    for j in range(m):
        for i in range(n):
            if not field[i][j] == 0:
                drill[j].append(field[i][j])
    #각 열을 시추할 때 얻을 수 있는 석유의 양 계산
    for col in drill:
        oil = 0
        for pos in set(col):
            oil += olis[pos]
        answer = oil if oil > answer else answer
    print(answer)