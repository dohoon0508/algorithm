def solution(s):
    zero_count = 0
    circle = 0
    
    while s != "1":
        circle += 1
        zero_count += s.count('0')
        s = s.replace("0", "")
        s = bin(len(s))[2:]
            
    
    
    return [circle, zero_count]