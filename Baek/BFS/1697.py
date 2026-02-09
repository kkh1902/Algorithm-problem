"""
문제 : 1697 - 숨바꼭질

1. 아이디어
- BFS로 각 위치까지의 최소 시간을 계산한다.
- N >= K인 경우는 뒤로 걷기만 하면 되므로 N-K가 정답이다.

2. 시간복잡도
- O(최대좌표) = O(100000)

3. 자료구조
- 큐(BFS), 거리 배열
"""

from collections import deque

def bfs(n, k):
    MAX = 100000
    visited = [False] * (MAX + 1)

    q = deque()
    q.append((n, 0))   # (현재 위치, 시간)
    visited[n] = True

    while q:
        x, time = q.popleft()

        if x == k:
            return time

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = True
                q.append((nx, time + 1))


n, k = map(int, input().split())
print(bfs(n, k))

