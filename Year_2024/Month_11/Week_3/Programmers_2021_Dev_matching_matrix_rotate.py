import heapq


def solution(rows, columns, queries):
    answer = []
    matrix = [[(i*columns + j) for j in range(1,columns+1)] for i in range(rows)]
    for query in queries:
        q = []
        x1,y1,x2,y2 = map(lambda x:x-1,query)
        temp = matrix[x1][y1]
        for i in range(x1,x2):
            matrix[i][y1] = matrix[i+1][y1]
            heapq.heappush(q,matrix[i+1][y1])
        for j in range(y1,y2):
            matrix[x2][j] = matrix[x2][j+1]
            heapq.heappush(q, matrix[x2][j+1])
        for k in range(x2,x1,-1):
            matrix[k][y2] = matrix[k-1][y2]
            heapq.heappush(q, matrix[k-1][y2])
        for l in range(y2,y1+1,-1):
            matrix[x1][l] = matrix[x1][l-1]
            heapq.heappush(q, matrix[x1][l-1])
        matrix[x1][y1+1] = temp
        heapq.heappush(q, temp)
        answer.append(heapq.heappop(q))

    return answer