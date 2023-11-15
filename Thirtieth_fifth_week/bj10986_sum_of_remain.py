import sys
def solution():
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    remainders = [0 for _ in range(m)]

    total = 0
    for i in range(n):
        total += nums[i]
        r = total % m
        remainders[r] += 1

    answer = remainders[0]
    for j in remainders:
        answer += j * (j-1) // 2

    print(answer)

    # answer = 0
    #
    # for i in range(n):
    #     sum = 0
    #     for j in range(i, n):
    #         if i == j:
    #             sum += nums[i]
    #             if sum % m == 0:
    #                 answer += 1
    #         else:
    #             sum += nums[j]
    #             if sum % m == 0:
    #                 answer += 1
    # print(answer)


