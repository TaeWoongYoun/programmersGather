def solution(people, limit):
    people.sort() 
    count = 0
    front, end = 0, len(people) - 1
    while front <= end:
        if people[front] + people[end] <= limit:
            front += 1
        end -= 1
        count += 1
    return count