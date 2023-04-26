def solution(N, K):
    answer = 0
    temp = N

    while temp != 1:
        if temp % K == 0:
            temp /= K
            answer += 1
        else:
            temp -= 1
            answer += 1

    return answer
