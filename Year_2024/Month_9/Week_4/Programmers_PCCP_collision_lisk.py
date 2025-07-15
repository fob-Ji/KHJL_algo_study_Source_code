import copy


def solution(points, routes):
    answer = 0

    cur = []
    goal = []
    # for route in routes:
    #     temp = list()
    #     for point in route:
    #         temp.append(points[point-1])
    #     goal.append(temp)
    dy_route = []
    def loc(num):
        return tuple(points[num-1])

    def mov(start,end):
        r,c = start
        if not start[0] == end[0]:
            if start[0] < end[0]:
                r += 1
            else:
                r -= 1
        else:
            if start[1] < end[1]:
                c += 1
            else:
                c -= 1
        return (r, c)

    for i in range(len(routes)):
        cur.append(tuple(loc(routes[i][0])))
        goal.append(routes[i][1:])

    while len(goal) != 0:
        for i in range(len(cur)):
            if not len(goal[i]):
                cur[i] = cur[:]
                continue
            if loc(goal[i][0]) == cur[i]:
                goal[i] = goal[i][1:]
            else:
                cur[i] = mov(cur[i], loc(goal[i][0]))
        loc_set = set(cur)
        for a in loc_set:
            if cur.count(a) > 1:
                answer += 1

    return answer
