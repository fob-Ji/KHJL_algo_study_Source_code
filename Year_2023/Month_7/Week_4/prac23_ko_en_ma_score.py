def solution():
    lst = []
    n = int(input())
    for i in range(n):
        name, ko, en, math = map(str, input().split())
        lst.append([name, int(ko), int(en), int(math)])

    # f = open("EighteenthWeek/input_23.txt")
    # n = int(f.readline())
    #
    # for i in range(n):
    #     name, ko, en, math = f.readline().split()
    #     lst.append([name, int(ko), int(en), int(math)])
    # f.close()
    lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    for i in range(n):
        print(lst[i][0])


