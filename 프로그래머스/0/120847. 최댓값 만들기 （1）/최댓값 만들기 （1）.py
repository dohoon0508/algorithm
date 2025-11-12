def solution(numbers):
    numbers.sort()
    big = numbers[-1]
    bigg = numbers[-2]
    
     
    answer = big * bigg
    return answer