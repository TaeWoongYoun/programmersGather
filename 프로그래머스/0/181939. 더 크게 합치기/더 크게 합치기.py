def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    
    if ab >= ba :
        return int(str(a) + str(b))
    else :
        return int(str(b) + str(a))
