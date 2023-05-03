def solution(N,M,K,numbers):
    data = sorted(numbers)
    m = M
    first = data[N-1]
    second = data[N-2]

    answer = 0

    while True:
        for i in range(K):
            if m==0:
                break
            answer+= first
            m -=1
        if m==0:
            break
        answer += second
        m -=1

    return answer

