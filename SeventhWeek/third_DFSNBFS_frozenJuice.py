def solution(N,M,field):
    answer = 0
    def dfs(x,y):
        if x<0 or x>=N or y<0 or y>=M:
            return False
        if field[x][y] == 0:
            field[x][y] = 1

            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x,y+1)
            return True
        return False

    for i in range(N):
        for j in range(M):
            if dfs(i,j) == True:
                answer+=1

    return answer