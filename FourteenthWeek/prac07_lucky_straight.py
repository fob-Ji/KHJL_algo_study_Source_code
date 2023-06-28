def solution():
    n = str(input())
    mid = len(n)//2
    left = 0
    right = 0

    for i in range(mid):
        left += int(n[i])

    for j in range(mid,len(n)):
        right += int(n[j])

    print("LUCKY") if left == right else print("READY")