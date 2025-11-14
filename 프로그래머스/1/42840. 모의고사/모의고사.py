def solution(answers):
    answer = []
    n = len(answers) - 1
    
    s1 = [1, 2, 3, 4, 5]
    n1 = 5
    a1 = 0
    
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n2 = 8
    a2 = 0
    
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    n3 = 10
    a3 = 0
    
    while n>= 0 :
        if answers[n] == s1[n%5]:
            a1 += 1
        if answers[n] == s2[n%8]:
            a2 += 1
        if answers[n] == s3[n%10]:
            a3 += 1
        n -= 1
            
    m = max(a1, a2, a3)
    
    if a1 == m :
        answer.append(1)
    if a2 == m :
        answer.append(2)
    if a3 == m :
        answer.append(3)
    
    
            
    return answer