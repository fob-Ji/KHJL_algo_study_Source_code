import sys


def solution():
    n, m, k, s, t = map(int, sys.stdin.readline().split())
    course = [[] for _ in range(n+1)]
    lift = [[] for _ in range(n+1)]
    dp =[[-1] * k + 1 for _ in range(n+1)]

    for _ in range(m):
        a, b, time = map(int, sys.stdin.readline().split())
        course[a].append((b, time))
        lift[b].append((a, 0))

    def dp(i, k):
        if i == t and k == 0:
            return 0
        if dp[i][k] != -1:
            return dp[i][k]
        max_time = int(1e9)
        if k > 0 :
            for a, time in lift[i]:
                max_time = max(max_time, dp(a, k - 1))
        for b, t in course[i]:
            max_value = max(max_value, t + dp(b, k))
