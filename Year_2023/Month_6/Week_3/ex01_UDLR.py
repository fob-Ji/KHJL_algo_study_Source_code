def solution(N,planer):
    plans = planer.split(" ")
    x,y = 1,1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    mov_types = ['U','D','L','R']
    for direction in plans:
        for i in range(len(mov_types)):
            if direction == mov_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 1 or nx > N or ny < 1 or ny > N:
            continue
        else:
            x = nx
            y = ny

    return [x,y]