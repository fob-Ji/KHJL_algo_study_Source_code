'''
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
입출력 예
n	return
118372	873211
'''

def solution(n):
    answer = 0
    arr = []
    st = ''
    num = n

    while True:
        quo, remain = divmod(num,10)
        num = quo
        arr.append(remain)
        if num == 0:
            break

    arr.sort(reverse=True)
    for i in range(len(arr)):
        st += str(arr[i])
    answer = int(st)
    return answer