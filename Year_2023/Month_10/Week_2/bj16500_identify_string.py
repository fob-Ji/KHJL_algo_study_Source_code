def solution():
    s = str(input())
    s_list = list(s)

    n = int(input())
    dp = [0] * (len(s_list) + 1)
    dp[0] = 1

    words = []
    for _ in range(n):
        word = str(input())
        words.append(word)

    for i in range(len(s_list) + 1):
        for word in words:
            word_len = len(word)
            if i >= word_len and dp[i - word_len] == 1 and s_list[i - word_len:i] == list(word):
                dp[i] = 1

    if dp[len(s_list)]:
        print(1)
    else:
        print(0)
