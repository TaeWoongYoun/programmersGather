def solution(phone_number):
    length = len(phone_number)
    answer = '*' * (length - 4) + phone_number[-4:]
    return answer
