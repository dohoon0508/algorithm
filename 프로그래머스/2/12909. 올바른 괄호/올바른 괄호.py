from collections import deque

def solution(s):
    stack = deque()
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":
            if not stack :
                return False
            stack.pop()
    if not stack :
        return True
    else : return False
        