from collections import deque


def solution(n, paths, gates, summits):
    answer = [1e9,1e9]

    edges = [[] for _ in range(n+1)]

    for u,v,w in paths:
        edges[u].append((v,w))
        edges[v].append((u,w))



    min_intensity = 0
    for start in gates:
        q = deque()
        q.append((start,0,0))
        visited = [False] * (n + 1)
        visited[start] = True
        while q:
            node,weight,intens = q.popleft()
            for v,w in edges[node]:
                if visited[v] == False :
                    if v in gates:
                        continue
                    elif v in summits:
                        temp = w if w > intens else intens
                        if intens == answer[1]:
                            answer = [v,temp] if v < answer[0] else answer
                        elif intens < answer[1]:
                            answer = [v,temp]
                        else:
                            pass
                    else:
                        visited[v] = True
                        temp = intens if intens > w else w
                        q.append((v,w,temp))

    print(answer)