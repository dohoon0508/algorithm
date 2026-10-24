from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    now_w = 0
    
    while trucks or now_w > 0:
        answer+=1
        out_car = bridge.popleft()
        now_w -= out_car
        
        if trucks and now_w + trucks[0] <= weight:
            next_car = trucks.popleft()
            now_w += next_car
            bridge.append(next_car)
            
        else : 
            bridge.append(0)
    return answer