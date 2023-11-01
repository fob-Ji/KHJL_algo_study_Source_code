def solution():
    n = int(input())
    A = [[1, 1], [1, 0]]
    divisor = 1000000007

    # 행렬 곱셈 2*2 행렬
    def mul(a, b):
        result = [[0] * len(b[0]) for _ in range(2)]
        for i in range(2):
            for j in range(2):
                s = 0
                for z in range(2):
                    s += a[i][z] * b[z][j]
                result[i][j] = s % divisor
        return result

    def power(matrix, exp):
        if exp == 1:
            return matrix
        else:
            tmp = power(matrix,exp//2)
            if exp % 2:
                return mul(mul(tmp,tmp),matrix)
            else:
                return mul(tmp,tmp)

    print(power(A,n)[0][1])

