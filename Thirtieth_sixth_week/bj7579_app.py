def solution():
    n, m = map(int, input().split())
    byte_arr = list(map(int, input().split()))
    cost_arr = list(map(int, input().split()))
    dp = [[0 for _ in range(sum(cost_arr) + 1)] for _ in range(n)]
    result = sum(cost_arr)


    for i in range(n):
        for j in range(sum(cost_arr)):
            #i번째 앱의 cost가 j를 넘으면 종료 시킬 수 없기 때문에 이전값을 가져옴
            if cost_arr[i] > j:
                dp[i][j] = dp[i - 1][j]
            #i번째 앱의 cost가 j보다 작거나 같으념 종료 시킬 수 있음
            else:
                dp[i][j] = max(dp[i - 1][j], byte_arr[i] + dp[i - 1][j-cost_arr[i]])

            if dp[i][j] >= m: ## 구한 최대 메모리가 m을 만족시키는 지 체크
                result = min(result, j)
    if m != 0:
        print(result)
    else:
        print(0)