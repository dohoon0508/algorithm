from collections import Counter

def solution(k, tangerine):
    counters = Counter(tangerine)
    answer = 1
    count_t = 0
    sorted_con = sorted(counters.values(), reverse = True)
    
    for i in sorted_con :
        count_t += i
        if count_t >= k:
            return answer
        else : 
            answer += 1