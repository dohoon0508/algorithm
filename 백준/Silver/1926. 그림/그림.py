import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(input().strip().split()) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 탐색 함수 (넓이 계산 포함)
def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    grid[start_x][start_y] = "0"  # 방문 처리
    area = 1  # ✅ 1부터 시작해야 첫 번째 '1' 포함

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == "1":
                grid[nx][ny] = "0"
                queue.append((nx, ny))
                area += 1  #방문할 때마다 크기 증가

    return area


count = 0
max_area = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == "1":  # 방문하지 않은 '1' 발견
            current_area = bfs(i, j)  # BFS 탐색 시작
            count += 1  # 새로운 덩어리 개수 증가
            max_area = max(max_area, current_area)  # 가장 큰 넓이 업데이트


print(count)  
print(max_area)