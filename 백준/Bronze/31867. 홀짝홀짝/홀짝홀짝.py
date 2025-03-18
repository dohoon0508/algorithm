import sys
input = sys.stdin.readline

n = int(input().rstrip())
nl = list(map(int, input().rstrip()))
count = 0

for i in nl:
    if i % 2 == 0:
        count += 1
    else : count -= 1

if count > 0 :
    print("0")
elif count < 0 :
    print("1")
else : print("-1")