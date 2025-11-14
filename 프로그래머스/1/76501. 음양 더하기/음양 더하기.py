def solution(absolutes, signs):
    answer = 0
    
    n = len(absolutes)
    
    while n > 0:
        n -= 1
        if signs[n] == True :
            answer += absolutes[n]
        elif signs[n] == False :
            answer += absolutes[n] * (-1)
    
    return answer