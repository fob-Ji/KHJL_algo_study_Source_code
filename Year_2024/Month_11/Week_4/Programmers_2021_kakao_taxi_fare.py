import copy
from collections import deque
import heapq

def solution(n, s, a, b, fares):
    answer = 0
    edges = [[] for i in range(n+1)]
    for u, v, f in fares:
        edges[u].append((v, f))
        edges[v].append((u, f))
    q = deque()
    info = [a,0,[a]]
    q.append(info)
    visited = [False]* (n+1)
    a_info = []
    while q:
        u,fare_sum,route = q.popleft()
        for v,f in edges[u]:
            if visited[v] == False:
                temp_route = copy.deepcopy(route)
                temp_fare = fare_sum
                temp_fare += f
                temp_route.append(v)
                if v == s:
                    heapq.heappush(a_info,(fare_sum,temp_route))
                else:
                    q.append((v,temp_fare,temp_route))
        visited[u] = True


    return answer
