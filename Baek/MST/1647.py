"""
1. 아이디어
- 마을의 모든 집을 최소 비용으로 연결해야 하므로 최소 신장 트리(MST)를 만든다.
- Prim 알고리즘을 사용해 MST를 구성한다.
- MST는 N-1개의 간선으로 하나의 연결 그래프가 된다.
- 마을을 두 개로 분리하려면 MST에서 간선 하나를 제거하면 된다.
- 유지비 합을 최소로 하려면 MST에 포함된 간선 중 가장 비용이 큰 간선을 제거한다.
- 따라서:
  (MST 전체 비용) - (MST에서 가장 비싼 간선) 이 정답이다.

2. 시간 복잡도
- Prim 알고리즘 + 우선순위 큐 사용
- 모든 간선이 힙에 들어갈 수 있으므로 O(M log N)
- 문제 제한 내에서 충분히 통과 가능

3. 자료구조
- 인접 리스트(graph): 그래프 표현
- 최소 힙(priority queue): 가장 비용이 작은 간선 선택
- visited 배열: 방문 여부 체크 (사이클 방지)
"""

import sys
import heapq
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

# 방문 여부
visited = [False] * (N + 1)

# (간선 비용, 노드)
heap = [(0, 1)]

total_cost = 0   # MST 전체 비용
max_edge = 0     # MST에 포함된 간선 중 가장 큰 비용

while heap:
    cost, node = heapq.heappop(heap)

    # 이미 방문한 노드라면 건너뛴다 (사이클 방지)
    if visited[node]:
        continue

    # 처음 방문한 노드라면 MST에 포함
    visited[node] = True
    total_cost += cost
    max_edge = max(max_edge, cost)

    # 현재 노드와 연결된 간선들 확인
    for next_cost, next_node in graph[node]:
        if not visited[next_node]:
            heapq.heappush(heap, (next_cost, next_node))

# 가장 비싼 간선 하나 제거하여 두 개의 마을로 분리
print(total_cost - max_edge)
