def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)-9):
        day_10 = discount[i : i+10]
        a = len(want)
        for j in range(len(want)):
            if number[j] <= day_10.count(want[j]):
                a -=1
            if a == 0:
                answer+=1
            
    return answer