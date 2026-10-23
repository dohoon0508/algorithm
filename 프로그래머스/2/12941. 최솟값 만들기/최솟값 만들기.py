def solution(A,B):
    A.sort()
    B.sort()
    
    a = len(A)
    
    answer = 0
    
    for i in range(a):
        answer += A[i]*B[-1-i]
        


    return answer