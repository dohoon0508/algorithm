import sys

for line in sys.stdin:
    m, f = map(int, line.split())
    if m == 0 and f == 0:
        break
    print(m + f)
