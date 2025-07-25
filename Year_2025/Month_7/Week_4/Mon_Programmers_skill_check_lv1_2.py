'''
문제 설명
민수는 다양한 지폐를 수집하는 취미를 가지고 있습니다. 지폐마다 크기가 달라 지갑에 넣으려면 여러 번 접어서 넣어야 합니다. 예를 들어 지갑의 크기가 30 * 15이고 지폐의 크기가 26 * 17이라면 한번 반으로 접어 13 * 17 크기로 만든 뒤 90도 돌려서 지갑에 넣을 수 있습니다. 지폐를 접을 때는 다음과 같은 규칙을 지킵니다.

지폐를 접을 때는 항상 길이가 긴 쪽을 반으로 접습니다.
접기 전 길이가 홀수였다면 접은 후 소수점 이하는 버립니다.
접힌 지폐를 그대로 또는 90도 돌려서 지갑에 넣을 수 있다면 그만 접습니다.
지갑의 가로, 세로 크기를 담은 정수 리스트 wallet과 지폐의 가로, 세로 크기를 담은 정수 리스트 bill가 주어질 때, 지갑에 넣기 위해서 지폐를 최소 몇 번 접어야 하는지 return하도록 solution함수를 완성해 주세요.

지폐를 지갑에 넣기 위해 접어야 하는 최소 횟수를 구하는 과정은 다음과 같습니다.

1. 지폐를 접은 횟수를 저장할 정수 변수 answer를 만들고 0을 저장합니다.
2. 반복문을 이용해 bill의 작은 값이 wallet의 작은 값 보다 크거나 bill의 큰 값이 wallet의 큰 값 보다 큰 동안 아래 과정을 반복합니다.
    2-1. bill[0]이 bill[1]보다 크다면
        bill[0]을 2로 나누고 나머지는 버립니다.
    2-2. 그렇지 않다면
        bill[1]을 2로 나누고 나머지는 버립니다.
    2-3. answer을 1 증가시킵니다.
3. answer을 return합니다.
위의 의사코드와 작동방식이 다른 코드를 작성해도 상관없습니다.
제한사항
wallet의 길이 = bill의 길이 = 2
10 ≤ wallet[0], wallet[1] ≤ 100
10 ≤ bill[0], bill[1] ≤ 2,000
입출력 예
wallet	bill	result
[30, 15]	[26, 17]	1
[50, 50]	[100, 241]	4
입출력 예 설명
입출력 예 #1

지문과 동일합니다.
입출력 예 #2

지폐를 접으면 다음과 같이 크기가 줄어듭니다. 따라서 4번 접으면 지갑에 넣을 수 있습니다.
[100, 241] -> [100, 120] -> [100, 60] -> [50, 60] -> [50, 30]
cpp를 응시하는 경우 리스트는 배열과 동일한 의미이니 풀이에 참고해주세요.
ex) 번호가 담긴 정수 리스트 numbers가 주어집니다. => 번호가 담긴 정수 배열 numbers가 주어집니다.
java를 응시하는 경우 리스트는 배열, 함수는 메소드와 동일한 의미이니 풀이에 참고해주세요.
ex) solution 함수가 올바르게 작동하도록 한 줄을 수정해 주세요. => solution 메소드가 올바르게 작동하도록 한 줄을 수정해 주세요.
'''


def isPut(wallet, bill):
    if wallet[0] > wallet[1]:
        wallet_l = wallet[0]
        wallet_s = wallet[1]
    else:
        wallet_l = wallet[1]
        wallet_s = wallet[0]

    if bill[0] > bill[1]:
        bill_l = bill[0]
        bill_s = bill[1]
    else:
        bill_l = bill[1]
        bill_s = bill[0]
    if wallet_l >= bill_l and wallet_s >= bill_s:
        return True


def fold(bill):
    if bill[0] < bill[1]:
        bill[1] = bill[1] // 2
    else:
        bill[0] = bill[0] // 2
    return bill

def solution(wallet, bill):
    answer = 0
    while not isPut(wallet, bill):
        bill = fold(bill)
        answer += 1

    return answer

