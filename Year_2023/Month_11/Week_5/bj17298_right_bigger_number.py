import sys


def solution():
    n = int(sys.stdin.readline())
    sequence = list(map(int, sys.stdin.readline().split()))
    stack = []
    answer = [-1] * n

    for i in range(n):
        while stack and sequence[stack[-1]] < sequence[i]:
            answer[stack.pop()] = sequence[i]
        stack.append(i)

    print(*answer)

    # for i in range(n):
    #     for j in range(i, n):
    #         if stack[i] < stack[j]:
    #             print(stack[j], end=" ")
    #             break
    #         else:
    #             if j == n-1:
    #                 print(-1, end=" ")
