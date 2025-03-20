import sys
input = sys.stdin.readline

result = 0

while 1 :
    i = int(input().rstrip())
    if i == -1 :
        break
    else : result += i

print(result)
