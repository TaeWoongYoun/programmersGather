def solution(my_string, index_list):
    answer = ""
    for i in index_list:
        if i < len(my_string):
            answer += my_string[i]
    return answer