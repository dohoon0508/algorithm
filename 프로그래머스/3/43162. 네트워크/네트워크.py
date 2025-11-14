def solution(n, computers):
    visited = [False]*n
    answer = 0
    
    def dfs(x):
        visited[x] = True
        for y in range(n):
            if computers[x][y] == 1 and not visited[y]:
                dfs(y)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
    return answer