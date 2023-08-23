import sys


def solution():
    n, g, k = map(int, input().split())

    essential = []
    non_essential = []

    for _ in range(n):
        decay, expiration, is_important = map(int, sys.stdin.readline().split())
        if is_important:
            non_essential.append([decay, expiration])
        else:
            essential.append([decay, expiration])

    start = 0
    end = int(2e9)
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        germ = 0

        if len(non_essential) > k:
            non_essential.sort(key=lambda x: -(x[0] * max(1, mid-x[1])))
            for i in range(k, len(non_essential)):
                germ += non_essential[i][0] * max(1, mid-non_essential[i][1])
        for j in range(len(essential)):
            germ += essential[j][0] * max(1, mid - essential[j][1])
        if germ <= g:
            answer = max(answer, mid)
            start = mid+1
        else:
            end = mid-1
    print(answer)


