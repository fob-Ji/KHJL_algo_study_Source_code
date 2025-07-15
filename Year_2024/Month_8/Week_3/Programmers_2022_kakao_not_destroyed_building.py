


def solution(board, skill):
    answer = 0
    destroyed = 0
    # min_r, min_c, max_r, max_c = 1e9, 1e9, -1, -1
    skill.sort(key=lambda x: x[0], reverse=True)
    for sk in skill:
        type, r1, c1, r2, c2, degree = sk
        # min_r = r1 if r1 < min_r else min_r
        # min_c = c1 if c1 < min_c else min_c
        # max_r = r2 if r2 > max_r else max_r
        # max_c = c2 if c2 > max_c else max_c
        if type == 2:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                # restored = False
                # if board[r][c] < 1:
                #     restored = True
                    board[r][c] += degree
                # if restored and board[r][c] > 0:
                #     destroyed -= 1
        else:
            for r in range(r1,r2+1):
                for c in range (c1,c2+1):
                    already_destroyed = False
                    if board[r][c] < 1:
                        already_destroyed = True
                    board[r][c] -= degree
                    if board[r][c] < 1 and not already_destroyed:
                        destroyed += 1


    answer = (len(board)*len(board[0])) - destroyed
    # answer += (len(board)*len(board[0]) - (max_r-min_r+1)*(max_c-min_c+1))
    # for row in range(min_r, max_r+1):
    #     for col in range(min_c, max_c+1):
    #         if board[row][col] > 0:
    #             answer += 1
    # return answer
    print(answer)