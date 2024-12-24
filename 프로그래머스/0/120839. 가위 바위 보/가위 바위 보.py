def solution(rsp):
    a = list(rsp)
    answer = ''
    for j in range(len(a)):
        if a[j] == '2':
            answer += '0'
        elif a[j] == '0':
            answer += '5'
        else:
            answer += '2'
    return answer