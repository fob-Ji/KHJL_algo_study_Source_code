def solution():
    n = int(input())
    queens = [0] * n
    answer = 0

    def is_valid(row):
        flag = True
        for r in range(row):
            if flag:
                if queens[row] == queens[r] or abs(queens[row] - queens[r]) == row - r:
                    flag = False
                    return False
            else:
                break
        return True

    def put_queen(x):
        global answer

        if x == n:
            answer += 1
            return

        for i in range(n):
            queens[x] = i
            if is_valid(x):
                put_queen(x+1)

    put_queen(0)
    print(answer)

