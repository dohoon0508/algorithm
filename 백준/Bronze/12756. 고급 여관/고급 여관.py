import sys
input = sys.stdin.readline

at, ap = map(int, input().rsplit())
bt, bp = map(int, input().rsplit())

while ap > 0 and bp > 0 :
    ap -= bt
    bp -= at
    if ap <= 0 and bp <= 0 :
        print("DRAW")
    elif ap > 0 and bp <= 0:
        print("PLAYER A")
    elif ap <= 0 and bp >= 0 :
        print("PLAYER B")
    else: pass