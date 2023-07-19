import heapq
def solution():
    n = int(input())
    heap = []
    for i in range(n):
        heapq.heappush(heap,int(input()))

    answer = 0
    while len(heap) != 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged_card = a+b
        answer += merged_card
        heapq.heappush(heap,merged_card)
    print(answer)