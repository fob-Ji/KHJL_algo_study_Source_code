def solution(N,K):
    answer = 0
    d = [0] * 100

    d[0] = K[0]
    d[1] = max(K[0],K[1])
    for i in range (2,N):
        d[i] = max(d[i-1], d[i-2] + K[i])

    answer = d[N-1]
    return answer