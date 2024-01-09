import sys


def solution():
    N, M, K = map(int, sys.stdin.readline().split())
    candies = [0] + list(map(int, sys.stdin.readline().split()))
    parents = [i for i in range(N+1)]
    friends = [1] * (N+1)
    dp = [0 for _ in range(K)]

    def find(a):
        if parents[a] != a:
            parents[a] = find(parents[a])
        return parents[a]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x < y:
            x, y = y, x
        parents[x] = y
        # if x < y:
        #   parents[y] = x
        # else:
        #   parents[x] = y

    def rob():
        for i in range(1, N+1):
            if i != parents[i]:
                continue
            for j in range(K-1, friends[i]-1, -1):
                dp[j] = max(dp[j], dp[j-friends[i]] + candies[i])

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        union(a, b)

    for j in range(1, N+1):
        if j != parents[j]:
            root = find(j)
            candies[root] += candies[j]
            friends[root] += friends[j]

    rob()
    print(max(dp))