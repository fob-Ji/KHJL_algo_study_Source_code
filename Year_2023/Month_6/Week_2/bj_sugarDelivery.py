def solution():
    n = int(input())
    left_weight = 0

    bag_3 = 0
    bag_5 = 0

    answer = -1

    for i in reversed(range(n//5+1)):
        bag_5 = i
        left_weight = n - 5 * bag_5
        bag_3 = left_weight // 3
        left_weight = left_weight - 3 * bag_3
        if left_weight == 0:
            answer = bag_3 + bag_5
            break

    print(answer)


