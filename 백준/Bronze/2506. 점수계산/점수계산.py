import sys
input = sys.stdin.readline

n = int(input().rstrip())
case = list(map(int, input().split()))
result = 0
w = 1

for i in case:
    if i == 1 :
        result += w
        w+=1
    else : w = 1

print(result)