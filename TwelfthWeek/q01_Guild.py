def solution():
    n = int(input())
    fears = list(map(input().split()))

    answer = 0
    count = 0
    fears.sort()

    for i in fears:
        count += 1
        if count >= i:
            answer += 1
            count = 0

    print(answer)
