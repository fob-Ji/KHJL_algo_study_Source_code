def solution(N):
    dp = [0] * 1001

    dp[1] = 1
    dp[2] = 3
    for i in range(3, N+1):
        dp[i] = (dp[i-1]+2*dp[i-2]) % 796796

    return dp[N]