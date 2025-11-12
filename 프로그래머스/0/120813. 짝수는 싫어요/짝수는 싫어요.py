def solution(n):
    mo = n/2
    
    answer = []
    
    m = 0
    
    while mo > 0:
        answer.append(1+ (m*2))
        m = m + 1
        mo = mo - 1
        
    return answer