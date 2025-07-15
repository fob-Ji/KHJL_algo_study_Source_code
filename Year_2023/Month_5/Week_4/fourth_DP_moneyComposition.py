def solution(N,M,Moneys):
    d = [10001] * [M+1]

    d[0] = 0
    for i in range(N):
        for j in range(Moneys[i],M+1):
            if d[j-Moneys[i]]!= 10001 :
                d[j] = min(d[j],d[j-Moneys[i]]+1)

    return d[M] if d[M] != 10001 else -1