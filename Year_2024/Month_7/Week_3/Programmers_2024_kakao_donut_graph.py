

def solution(edges):
    answer = []
    graph = [[] for _ in range(len(edges)+1)]
    visited = [False] * len(graph)
    for edge in edges:
        u, v = edge
        graph[u].append(v)

    for i in range(len(graph)):
        # if len(graph[i])
    print(answer)

