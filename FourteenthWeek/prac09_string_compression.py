def solution():
    s = str(input())
    answer = float('inf')
    for i in range(1, len(s)+1):
        unit_size = i
        compressed_str = ''
        previous_unit = ''
        count = 1
        for j in range(len(s)):
            if (j+1)*i <= len(s):
                cur_unit = s[j*i:(j+1)*i]
                next_unit = s[(j+1)*i:(j+2)*i]
                if cur_unit == next_unit:
                    count += 1
                else:
                    if count > 1:
                        compressed_str += str(count) + cur_unit
                        count = 1
                    else:
                        compressed_str += cur_unit
            else:
                compressed_str += s[j*i:]
        answer = min(answer, len(compressed_str))
    print(answer)

