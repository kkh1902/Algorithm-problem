"""
1. 아이디어
- N×N 격자를 전체 순회한다
- 아직 방문하지 않은 집(값이 1)을 만나면 BFS를 시작한다
- 상하좌우로 연결된 집들을 하나의 단지로 탐색한다
- BFS 한 번이 하나의 단지를 의미한다
- 각 단지마다 집의 개수를 센다

2. 시간복잡도
- O(N²)
- N×N 격자의 모든 칸을 최대 한 번씩 방문한다

3. 자료구조
- 지도 크기 : int (N)
- 지도 배열 : 2차원 리스트 (N×N)
- 방문 배열 : 2차원 boolean 리스트 (N×N)
- 단지 수 : int (cnt)
- 각 단지의 집 수 저장 리스트 : list (home_cnt)
- 탐색용 자료구조 : queue (BFS) 또는 재귀/stack (DFS)

"""

import sys
from collections import deque
input = sys.stdin.readline
n= int(input())

maps = [list(map(int, input().strip())) for _ in range(n)]

check = [[False] * n for _ in range(n)]
cnt = 0
home_cnt= []

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y,x):
    qu_cnt =1
    q = deque()
    q.append((y,x))
    check[y][x] = True

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny < n and 0 <= nx <n:
                if maps[ny][nx] == 1 and check[ny][nx] ==False:
                    check[ny][nx] = True
                    q.append((ny,nx))
                    qu_cnt +=1
    return qu_cnt

for i in range(n):
    for j in range(n):
        if maps[j][i] == 1 and check[j][i] == False:
            cnt+=1
            home_cnt.append(bfs(j,i))

print(cnt)
home_cnt.sort()
for i in home_cnt:
    print(i)