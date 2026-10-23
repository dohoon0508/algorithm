from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    all_num = 0
    answer = 1
    
    sorted_count = sorted(count.values(), reverse = True)
    
    for i in sorted_count:
        all_num += i
        if all_num >= k:
            return answer
        else : 
            answer+=1