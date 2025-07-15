def solution():
    n = int(input())
    info = list(map(int, input().split()))
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if info[i] < info[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(len(info) - max(dp))
