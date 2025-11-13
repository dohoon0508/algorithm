def solution(x):
    str(x)
    a = sum(int(i)for i in str(x))
    answer = True
    
    if x%a == 0:
        answer = True
    else : answer = False
        
    return answer