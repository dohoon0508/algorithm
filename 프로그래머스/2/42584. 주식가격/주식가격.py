def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)-1) :
        a = i
        while a != (len(prices)-1):
            a += 1
            
            if prices[i] <= prices[a]:
                answer[i] += 1
            else : 
                answer[i] += 1
                break
        
    
    
    
    return answer