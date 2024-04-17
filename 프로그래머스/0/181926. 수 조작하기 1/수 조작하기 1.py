def solution(n, control):
    answer = 0
    
#     딕셔너리 사용
    new = {
        "w": 1,
        "s": -1,
        "d": 10,
        "a": -10,
    }
    
    for i in control:
        n += new[i]

    return n