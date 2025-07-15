def solution1(n, m):
    result = 0

    for i in range(n):
        data = list(map(int, input().split()))

        min_value = min(data)

        result = max(result, min_value)
    return result


def solution2(n, m):
    result = 0

    for i in range(n):
        data = list(map(int, input().split()))
        # 입력 조건에 1부터 10000까지의 자연수이므로 max value로 초기화 할 때 10001 사용
        min_value = 10001
        for a in data:
            min_value = a if a < min_value else min_value
        result = result if result > min_value else min_value

    return result
