def solution():
    s = str(input())
    lst = []
    num = 0
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            lst.append(s[i])
        else:
            num += int(s[i])

    sorted_lst = sorted(lst)
    print(''.join(sorted_lst) + str(num))
