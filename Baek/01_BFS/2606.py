"""
1. 아이디어
- 1번 컴퓨터에서 시작해서 BFS 탐색을 한다
- 연결된 컴퓨터를 따라가며 감염되는 컴퓨터를 방문한다
- 이미 방문한 컴퓨터는 다시 방문하지 않는다
- 시작점인 1번 컴퓨터는 제외하고 방문한 개수만 센다

2. 시간복잡도
- O(N + M)
  - N: 컴퓨터 수
  - M: 연결된 쌍의 수
  - 모든 컴퓨터와 연결을 최대 한 번씩만 확인한다

3. 자료구조
- 컴퓨터 수 : int (N)
- 연결된 쌍 수 : int (M)
- 그래프 : 인접 리스트 (list of list)
- 방문 체크 : boolean 배열 또는 set
- 탐색용 자료구조 : queue (BFS)
- 감염된 컴퓨터 수 : int


"""

import sys
from collections import deque
input = sys.stdin.readline

# 1️⃣ 기본 입력
n = int(input())   # 컴퓨터 수
m = int(input())   # 연결된 쌍 수

# 2️⃣ 그래프 (인접 리스트)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 3️⃣ 방문 체크 배열
visited = [False] * (n + 1)

# 4️⃣ BFS 탐색용 큐
queue = deque()

# 5️⃣ 감염된 컴퓨터 수
count = 0

visited[1] = True
queue.append(1)

while queue:
    node = queue.popleft()

    for next in graph[node]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)
            count+=1

print(count)

