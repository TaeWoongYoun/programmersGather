def not_num(num):
    return  '1'  not in str(num) and '2'  not in str(num) and '3'  not in str(num) and '4'  not in str(num) and '6'  not in str(num) and '7'  not in str(num) and '8'  not in str(num) and '9'  not in str(num)

def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        if not_num(i):
            answer.append(i)
            
    if answer == []:
        return [-1]
    
    return answer

# def solution(l, r):
#     return [num for num in range(l, r+1) if '5' in str(num) and '0' in str(num)]