"""
아이디어
- 시작 정점 V부터 DFS, BFS 수행
- 방문하지 않은 정점만 탐색
- 방문 순서 출력을 위해 인접 리스트 정렬

시간복잡도
- DFS: O(N + M)
- BFS: O(N + M)

자료구조
- 그래프: 인접 리스트
- DFS: 재귀 함수
- BFS: deque
"""


# 문제풀이
from collections import deque

# 입력
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
"""
graph[0] = []
graph[1] = [2, 3, 4]
graph[2] = [1, 4]
graph[3] = [1, 4]
graph[4] = [1, 2, 3]
"""
# 번호 작은 것부터 방문
for i in range(1, N + 1):
    graph[i].sort()

# DFS
visited = [False] * (N + 1)
# 정점 번호를 그대로 쓰기위해 0번째 칸은 있긴하지만 쓰지않음

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt)

# BFS
def bfs(v):
    visited = [False] * (N + 1)
    q = deque([v])
    visited[v] = True

    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

# 실행
dfs(V)
print()
bfs(V)
