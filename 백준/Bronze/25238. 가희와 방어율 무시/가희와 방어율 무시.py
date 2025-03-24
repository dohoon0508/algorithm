import sys
input = sys.stdin.readline

att, am = map(int, input().rsplit())

result = att / 100 * (100-am)

if result < 100 : 
    print("1")
else : print("0")