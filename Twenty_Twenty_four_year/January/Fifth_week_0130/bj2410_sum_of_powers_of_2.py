def solution():
    N = int(input())

    dp = [0] * 1000001

    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        if i % 2 == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i//2]

    print(dp[N] % 1000000000)

