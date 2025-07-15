def solution(N,Exists,M,Requests):
    n = N
    exists = set(Exists)
    m = M
    requests = Requests
    for i in requests:
        if i in exists:
            print("yes", end=" ")
        else:
            print("no", end=" ")
