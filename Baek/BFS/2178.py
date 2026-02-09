from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs():
    q = deque()
    q.append((0,0))

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if maze[ny][nx] == 1:
                    maze[ny][nx] = maze[y][x] + 1
                    q.append((ny,nx))

bfs()
print(maze[n-1][m-1])
