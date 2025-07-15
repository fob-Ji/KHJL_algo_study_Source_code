def solution(play_time, adv_time, logs):
    answer = 0
    max_value = -1
    def timeToSec(time):
        H, M, S = map(int, time.split(':'))
        return (3600 * H + 60 * M + S)
    def secToTime(sec):
        q, remind = divmod(sec,60)
        s = remind
        q, remind = divmod(q,60)
        m = remind
        h = q
        rt = '{0:02d}:{1:02d}:{2:02d}'.format(h,m,s)
        return rt
    play_time_sec = timeToSec(play_time)
    adv_time_sec = timeToSec(adv_time)
    starting_point = 0
    max_starting_point = play_time_sec - adv_time_sec
    viewer = [[[0 for _ in range(60)] for _ in range(60)] for _ in range(100)]
    viewer_s = [0 for _ in range(360000)]
    for i in range(len(logs)):
        s_H,s_M,s_S = map(int,logs[i].split('-')[0].split(':'))
        e_H,e_M,e_S = map(int,logs[i].split('-')[1].split(':'))
        # viewer[s_H][s_M][s_S] += 1
        # viewer[e_H][e_M][e_S] -= 1
        viewer_s[s_H*3600 + s_M*60 + s_S] += 1
        viewer_s[e_H*3600 + e_M*60 + e_S] -= 1

    prefix_sum = [0 for _ in range(100*3600)]
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = viewer_s[i-1] + viewer_s[i]
    for j in range(max_starting_point+1):
        if max_value < sum(prefix_sum[j:j+adv_time_sec+1]):
            answer = j
            max_value = sum(prefix_sum[j:j+adv_time_sec+1])
    answer = secToTime(answer)

    viewer = sorted(logs)
    cur_viewer = 0
    for s,e in viewer:

    prefix_sum = [0 for _ in range(len(viewer)*2)]

    return answer

