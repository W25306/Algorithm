from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,graph):
    queue = deque()
    queue.append((x,y))
    n = len(graph)
    m = len(graph[0])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx< 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    if graph[n-1][m-1] == 1:
        return -1
    return graph[n-1][m-1]
    

def solution(maps):
    answer = 0
    
    
    return bfs(0,0,maps)
