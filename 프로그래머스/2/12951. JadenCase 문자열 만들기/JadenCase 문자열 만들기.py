def solution(s):
    s = s.lower()
    s_list = list(s)
    
    if s_list and s_list[0].islower():
        s_list[0] = s_list[0].upper()
        
    for i in range(len(s_list)):
        if i + 1 < len(s_list) and s_list[i] == " " and s_list[i+1].islower():
            s_list[i+1] = s_list[i+1].upper()

    return "".join(s_list)