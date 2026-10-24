from collections import Counter

def solution(k, tangerine):
    answer = 0
    sum_tan = 0
    
    coll_tan = Counter(tangerine)
    sorted_tan = sorted(coll_tan.values(), reverse = True)
    
    for i in sorted_tan:
        answer += 1
        sum_tan += i
        if k <= sum_tan:
            return answer