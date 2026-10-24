from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    sum_w = 0
    trucks = deque(truck_weights)
    
    while trucks or sum_w > 0:
        answer += 1
        
        out_truck = bridge.popleft()
        sum_w -= out_truck
        
        if trucks :
            if sum_w + trucks[0] <= weight:
                next_truck = trucks.popleft()
                bridge.append(next_truck)
                sum_w += next_truck
            else:
                bridge.append(0)
            
        
    return answer