def solution(n):
    
    answer = []   
    answer = list(str(n))
    
    answer = [int(i) for i in answer[::-1]]
    
    return answer
