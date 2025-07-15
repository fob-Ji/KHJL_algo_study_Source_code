def solution(n):
    answer = 0
    l = 0
    r = 50000000000000

    while l < r:
        m = (l + r) // 2
        if (n / m) < m:
            r = m
        elif (n / m) > m:
            if m ==1:
                answer = -1
                break
            l = m + 1
        elif (n / m) == m:
            answer = (m + 1) * (m + 1)
            break
        else:
            answer = -1


    return answer