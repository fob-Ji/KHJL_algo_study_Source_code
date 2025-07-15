def convert_to_decimal(base, exp):
    result = 0
    pwr = 0
    quot = int(exp)
    while quot > 0:
        quot, remain = divmod(quot, 10)
        result += pow(base, pwr) * remain
        pwr += 1
    return result

def convert_to_other(base, exp):
    result = ''
    quot = int(exp)
    while quot > 0:
        quot, remain = divmod(remain, base)
        result += str(quot)
    result += str(remain)
    return result

def find_base(opd1,opr,opd2,result):
    candidates = []

    for i in range(9, 1, -1):
        base = i
        operand1 = convert_to_decimal(i,opd1)
        operand2 = convert_to_decimal(i,opd2)
        ret = convert_to_decimal(i,result)

        if opr == "+":
            if operand1 + operand2 == ret:
                candidates.append(i)
        else:
            if operand1 - operand2 == ret:
                candidates.append(i)

    return candidates



def solution(expressions):
    answer = []
    base = -1

    variables = []

    for exp in expressions:
        opd1, opr, opd2, eql, result = exp.split(' ')
        if result == "X":
            variables.append(exp)
            continue

        bases = find_base(opd1, opr, opd2, result)
        if len(bases) == 1:
            base = bases[0]

    for var in variables:
        opd1, opr, opd2, eql, result = var.split(' ')
        if opr == "+":
            temp = convert_to_decimal(base,opd1) + convert_to_decimal(base,opd2)
            result = convert_to_other(base,temp)
        else:
            temp = convert_to_decimal(base, opd1) - convert_to_decimal(base, opd2)
            result = convert_to_other(base, temp)

        str = opd1 + ' ' + opr + ' ' + opd2 + ' ' + eql + ' ' + result
        answer.append(str)

    return answer