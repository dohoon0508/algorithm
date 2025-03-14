import sys
from collections import deque


M, N = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
            grid[nx][ny] = grid[x][y] + 1  
            queue.append((nx, ny))

max_days = 0
for row in grid:
    if 0 in row: 
        print(-1)
        exit(0)
    max_days = max(max_days, max(row))

print(max_days - 1 if max_days > 1 else 0)
