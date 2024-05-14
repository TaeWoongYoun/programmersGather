def solution(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a+b 
    # if n == 0:
    #     return 0
    return b % 1234567