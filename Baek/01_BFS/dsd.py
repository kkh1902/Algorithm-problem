import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

maps = [list(map(int, input().strip())) for _ in range(n)]
check = [[False] * n for _ in range(n)]

cnt = 0
home_cnt = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    qu_cnt = 1
    q = deque()
    q.append((y, x))
    check[y][x] = True   # ✅ 시작점 방문 처리

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < n:
                if maps[ny][nx] == 1 and not check[ny][nx]:
                    check[ny][nx] = True
                    q.append((ny, nx))
                    qu_cnt += 1
    return qu_cnt


for i in range(n):
    for j in range(n):
        if maps[j][i] == 1 and not check[j][i]:
            cnt += 1
            home_cnt.append(bfs(j, i))   # ✅ 반환값 저장

home_cnt.sort()

print(cnt)
for x in home_cnt:
    print(x)
