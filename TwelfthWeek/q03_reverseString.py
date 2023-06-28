def solution():
    s = input()

    toZero = 0
    toOne = 0

    if s[0] == '1':
        toZero += 1
    else:
        toOne += 1

    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i+1] == '1':
                toZero += 1
            else:
                toOne += 1

    print(min(toZero,toOne))









