def solution(price, money, count):
    answer = 0
    
    for i in range(1, count+1):
        answer += price * i
    
    if answer >= money:
        answer = abs(money - answer)
    else:
        return 0    
        
    return answer