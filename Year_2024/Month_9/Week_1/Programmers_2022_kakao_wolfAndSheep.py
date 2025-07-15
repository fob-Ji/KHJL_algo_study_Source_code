from collections import deque


def solution(info, edges):
    answer = 0
    edge = [[] for _ in range(18)]
    for u, v in edges:
        edge[u].append(v)

    visited = [False]*18
    wolfs = 0
    q = deque()
    q.append(0)
    while q:
        node = q.popleft()
        if info[node] == 0:
            answer += 1
            visited[node] = True
            for leaf in edge[node]:
                q.append(leaf)
        else:
            if answer - 1 > wolfs and visited[node] == False:
                wolfs += 1
                visited[node] = True
                if len(edge[node]) == 0:
                    wolfs -=1
                for leaf in edge[node]:
                    q.append(leaf)
            elif visited[node] == True:
                pass
            else:
                q.append(node)

    return answer