def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    graph = dict()
    for i in range(len(enroll)):
        key = enroll[i]
        value = referral[i]
        graph[key] = (i,value)

    for i in range(len(seller)):
        s = seller[i]
        income = amount[i] * 100
        interest = income // 10
        profit = income - interest
        answer[graph[s][0]] += profit
        while not graph[s][1] == "-":
            s = graph[s][1]
            income = interest
            interest = income // 10
            profit = income - interest
            answer[graph[s][0]] += profit
            if interest == 0:
                break
    return answer