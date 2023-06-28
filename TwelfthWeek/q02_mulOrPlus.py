def solution():
    str_number = input()
    numbers = [int(i) for i in str_number]


    answer = max(numbers[0]+numbers[1], numbers[0]*numbers[1])
    for i in range(2,len(numbers)):
        operand1 = answer
        operand2 = numbers[i]

        sum = operand1 + operand2
        mul = operand1 * operand2

        answer = sum if sum > mul else mul

    print(answer)
