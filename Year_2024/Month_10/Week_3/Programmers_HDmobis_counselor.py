from collections import deque
import heapq

def solution(k, n, reqs):
    answer = 0
    couns = [1]*(k+1)
    fr = n - k
    waitng = deque()
    consulting = []
    for req in reqs:
        clock, elapse, typ = req
        while True:
            if consulting:
                counselor = heapq.heappop(consulting)
                if counselor[0] < clock:
                    couns[counselor[1]] += 1
                    del_list = []
                    for i in range(len(waitng)):
                        w_c, w_e, w_t = waitng[i]
                        if couns[w_t] > 0:
                            heapq.heappush(consulting,(w_c+w_e, w_t))
                            answer += counselor[0] - w_c
                            del_list.append(i)
                else:
                    heapq.heappush(consulting, counselor)
                    break
            else:
                break
        if couns[typ] > 0:
            heapq.heappush(consulting, (clock + elapse, typ))
            couns[typ] -= 1
        else:
            if fr > 0:
                # 여유 있으면 그 타입에 배정
                fr -= 1
                couns[typ] += 1
                heapq.heappush(consulting, (clock + elapse, typ))
                couns[typ] + - 1
            else:
                # 여유가 없으면 waitng
                waitng.append(req)

    for cons in consulting:
        counselor = cons
        couns[counselor[1]] += 1
        del_list = []
        for i in range(len(waitng)):
            w_c, w_e, w_t = waitng[i]
            if couns[w_t] > 0:
                heapq.heappush(consulting, (w_c + w_e, w_t))
                answer += counselor[0] - w_c
                del_list.append(i)

    print(answer)
        # waiting_req = waitng.popleft()

        # time += 1
        # counselor = heapq.heappop(consulting)
        # if time == counselor[0]:
        #     couns[counselor[1]] += 1
        # else:
        #     heapq.heappush(consulting)
        # answer += len(waitng)
        # if waitng:
        #     c,r,t = waitng.popleft()
        #
        #
        # if idx < len(reqs):
        #     clock, elapse, tp = reqs[idx]
        #     if time == clock:
        #         if couns[tp] > 0:
        #             heapq.heappush(consulting, (clock + elapse, tp))
        #             couns[tp] -= 1
        #         else:
        #             if fr > 0:
        #                 # 여유 있으면 그 타입에 배정
        #                 fr -= 1
        #                 couns[tp] += 1
        #                 heapq.heappush(consulting, (clock + elapse, tp))
        #                 couns[tp] + - 1
        #             else:
        #                 # 여유가 없으면 waitng
        #                 waitng.append(reqs[idx])
        #         idx += 1


