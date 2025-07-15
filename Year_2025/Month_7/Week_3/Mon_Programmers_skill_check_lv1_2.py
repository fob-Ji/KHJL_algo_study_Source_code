def solution(food):
    answer = ''
    arr = ''
    arr_reverse = ''
    for i in range(1,len(food)):
        for _ in range(food[i] // 2):
            arr += str(i)
    print(len(arr))
    for j in reversed(arr):
        arr_reverse += str(j)

    answer = arr + '0' + arr_reverse


    return answer