from collections import deque

def bfs(N, K):
    visited = [-1] * 100001  # 방문하지 않으면 -1
    queue = deque([N])
    visited[N] = 0  # 시작 위치의 시간 = 0초

    while queue:
        current = queue.popleft()

        if current == K:
            return visited[current]

        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1: 
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

N, K = map(int, input().split())
print(bfs(N, K))
