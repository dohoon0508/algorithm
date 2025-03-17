import sys

input = sys.stdin.readline
N = int(input().strip())

participants = []

for i in range(1, N + 1):
    S, C, L = map(int, input().split())
    participants.append((S, C, L, i)) 

participants.sort(key=lambda x: (-x[0], x[1], x[2]))

print(participants[0][3])
