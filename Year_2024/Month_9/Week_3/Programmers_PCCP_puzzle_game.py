def solution(diffs, times, limit):
    answer = 0

    left = 1
    right = 100000

    while left <= right:
        elapse = 0
        mid = (left + right) // 2
        for i in range(len(diffs)):
            if i == 0:
                if diffs[i] > mid:
                    elapse += (diffs[i] - mid) * times[i] + times[i]
                else:
                    elapse += times[i]
            else:
                if diffs[i] > mid:
                    elapse += (diffs[i] - mid)*(times[i-1]+times[i]) + times[i]
                else:
                    elapse += times[i]
        if elapse > limit:
            left = mid + 1
        else:
            right = mid - 1
    answer = left

    # while elapse > limit:
    #     answer += 1
    #     elapse = 0
    #     for i in range(len(diffs)):
    #         if i == 0:
    #             if diffs[i] > answer:
    #                 elapse += (diffs[i] - answer) * times[i] + times[i]
    #             else:
    #                 elapse += times[i]
    #         else:
    #             if diffs[i] > answer:
    #                 elapse += (diffs[i] - answer)*(times[i-1]+times[i]) + times[i]
    #             else:
    #                 elapse += times[i]
    print(answer)
    # return answer