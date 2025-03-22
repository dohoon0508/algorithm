import sys
input = sys.stdin.readline

day = int(input().rstrip())
am = int(input().rstrip())
ak = int(input().rstrip())
dm = int(input().rstrip())
dk = int(input().rstrip())

re_m = 0
re_k = 0

if am % dm == 0 :
    re_m = am // dm
else : re_m = am // dm + 1

if ak % dk == 0 :
    re_k = ak // dk
else : re_k = ak // dk + 1

if re_k >= re_m:
    day -= re_k
else : 
    day -= re_m

print(day)