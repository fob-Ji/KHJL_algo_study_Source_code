from collections import deque
def solution(N,stages):
    sorted_stages = deque(sorted(stages))
    stage = 1
    denominator = len(sorted_stages)
    numerator = 0
    failure_rates = []
    while sorted_stages:
        if sorted_stages[0] == stage:
            numerator += 1
            sorted_stages.popleft()
        else:
            failure_rates.append((numerator / denominator, stage))
            stage += 1
            denominator = len(sorted_stages)
            numerator = 0
    if len(failure_rates) < N:
        for i in range(stage, N + 1):
            if denominator != 0:
                failure_rates.append((numerator / denominator, stage))
                stage += 1
                denominator = len(sorted_stages)
            else:
                failure_rates.append((0, stage))
                stage += 1

    failure_rates.sort(key=lambda x: (-x[0], x[1]))

    # return list(map(lambda x: x[1], failure_rates))

    print(failure_rates)
    print(list(map(lambda x: x[1], failure_rates)))

