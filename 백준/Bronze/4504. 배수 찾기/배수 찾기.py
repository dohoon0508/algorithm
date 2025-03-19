import sys
input = sys.stdin.readline

m = int(input().rstrip())

while 1 :
    a = int(input().rstrip())
    if a == 0 :
        break
    elif a % m == 0:
        print("%d is a multiple of %d." %(a, m))
    elif a % m != 0 :
        print("%d is NOT a multiple of %d." %(a, m))