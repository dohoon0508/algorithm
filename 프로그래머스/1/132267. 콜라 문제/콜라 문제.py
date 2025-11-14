def solution(a, b, n):
    answer = 0
    na = 0
    
    while n >= a :
        answer += (n//a) * b
        na = n%a
        n = ((n//a)*b)+ na
    
    return answer