def solution(names):
    answer = []
    list_size = 5
    for i in range(0, len(names), list_size):
        answer.append(names[i])

    return answer