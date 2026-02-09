"""
1. 아이디어
- m x n 격자를 전체 순회한다.
- 아직 방문하지 않은 값을 만나면 dfs 시작
- 상하좌우로 연결된 점들을 하나로 탐색한다
- dfs 한번이 하나의 단지를 의미한다. 
- 끝날 때 단지 카운트를 한다.

2. 시간복잡도
- O(m x n )
- m x n  격자의 모든 칸을 최대 한 번씩 방문한다

3. 자료구조
- t : int 
- m ,n , k  : int   
가로길이 M(1 ≤ M ≤ 50) 
세로길이 N(1 ≤ N ≤ 50) 
위치의 개수 K(1 ≤ K ≤ 2500)
- 배추의 위치 : X, Y   X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)
- 지도 배열 : 2차원 리스트 (m x n)
- 방문 배열 : 2차원 boolean 리스트 (m x n)
- 배추 흰지렁이 마리 수 : int (cnt)
- 재귀 (DFS)
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

t = int(input())

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    visited[y][x] = True

    for k in range(4):
        ny = y+ dy[k]
        nx = x+ dx[k]
        if 0<=ny <n and 0<=nx<m and visited[ny][nx] == False and maps[ny][nx]==1:
            dfs(ny,nx)

for i in range(t):
    m,n, k = map(int,input().split())
    maps = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)] 
    cnt = 0
    for j in range(k):
        x, y = map(int,input().split())
        maps[y][x]=1
    
    # 모든 노드 돌면서 dfs 써서 돌기 

    # 바깥 for 는 세로 n
    for y in range(n):
        # 안쪽 for 는 가로 m
        for x in range(m):
            # 배추가 있는 칸인가 and 방문이 x 일때  
            # 방문 표시 하고 dfs 재귀
            if maps[y][x] == 1 and visited[y][x] == False:
                dfs(y,x)
                cnt+=1
    print(cnt)




