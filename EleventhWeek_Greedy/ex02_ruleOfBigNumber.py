def solution1(N,M,K,numbers):
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

def solution2(N,M,K,Numbers):
    data = sorted(Numbers)
    first = data[N-1]
    second = data[N-2]

    count = int(M / (K+1)) * K
    count += M % (M+1)

    answer = 0
    answer += count * first
    answer += (M-count) * second

    return answer
