def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        line = []
        for j in range(1):
            line.append(num_list[i:i+n])
        answer.append(line)
    return sum(answer,[])