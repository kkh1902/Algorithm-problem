"""
BOJ 1012 - 유기농 배추 (DFS)

1. 아이디어
- m x n 격자를 전체 순회한다.
- 배추(1)가 있고 아직 방문하지 않은 칸을 만나면 DFS 시작
- DFS로 상/하/좌/우로 연결된 모든 배추를 방문 처리
- DFS 한 번 = 흰지렁이 1마리
- DFS를 시작한 횟수를 센다

2. 시간복잡도
- O(m x n)
- 모든 칸을 최대 한 번씩만 방문

3. 자료구조
- maps: 배추 위치를 표시한 2차원 리스트 (n x m)
- visited: 방문 여부를 표시한 2차원 리스트 (n x m)
- dy, dx: 상하좌우 이동을 위한 방향 배열
- 재귀 DFS
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)  # 재귀 깊이 제한 증가 (최대 2500칸 대비)

# 테스트 케이스 수
t = int(input())

# 상, 우, 하, 좌 방향 이동
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(y, x):
    """
    (y, x) 위치에서 시작하여
    상하좌우로 연결된 모든 배추를 방문 처리하는 DFS
    """
    # 현재 칸 방문 표시
    visited[y][x] = True

    # 4방향 탐색
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        # 다음 칸이
        # 1) 범위 안에 있고
        # 2) 배추가 있으며
        # 3) 아직 방문하지 않았다면
        if (
            0 <= ny < n and
            0 <= nx < m and
            maps[ny][nx] == 1 and
            not visited[ny][nx]
        ):
            dfs(ny, nx)


for _ in range(t):
    # m: 가로 길이, n: 세로 길이, k: 배추 개수
    m, n, k = map(int, input().split())

    # 배추 지도 (0: 없음, 1: 있음)
    maps = [[0] * m for _ in range(n)]

    # 방문 여부 체크 배열
    visited = [[False] * m for _ in range(n)]

    # 흰지렁이 수
    cnt = 0

    # 배추 위치 입력
    for _ in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1  # (x, y) → maps[y][x]

    # 전체 격자 순회
    for y in range(n):        # 세로
        for x in range(m):    # 가로
            # 배추가 있고 아직 방문하지 않았다면
            if maps[y][x] == 1 and not visited[y][x]:
                dfs(y, x)     # 하나의 배추 군집 탐색
                cnt += 1      # 흰지렁이 1마리 추가

    print(cnt)
