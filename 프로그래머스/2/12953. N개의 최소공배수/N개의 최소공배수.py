def solution(arr):
    lcm_result = arr[0]
    
    for i in range(1, len(arr)):
        a = lcm_result
        b = arr[i]
        while b:            
            a, b = b, a % b #유클리드 호제법
        lcm_result = lcm_result * arr[i] // a
    
    return lcm_result