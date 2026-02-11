"""
문제 : 11403 (경로 찾기)

그래프에서 모든 정점 i에서 모든 정점 j로
이동 가능한 경로가 존재하는지 여부를 구하는 문제이다.

1. 아이디어
- 모든 정점 → 모든 정점의 도달 가능 여부를 확인해야 하므로
  플로이드-워셜 알고리즘을 사용한다.
- 인접 행렬을 그대로 사용하여,
  i -> k 로 갈 수 있고 k -> j 로 갈 수 있다면
  i -> j 도 갈 수 있다고 판단한다.
- 최단 거리나 비용은 필요 없고,
  경로 존재 여부만 판단하므로 0 / 1 값만 사용한다.

2. 시간 복잡도
- 플로이드 워셜 알고리즘은 3중 반복문을 사용하므로
  시간 복잡도는 O(N³)이다.
- N ≤ 100 이므로 충분히 수행 가능하다.

3. 자료구조
- 2차원 리스트(graph)를 사용하여 인접 행렬을 표현한다.
- graph[i][j] = 1 : i에서 j로 갈 수 있음
- graph[i][j] = 0 : i에서 j로 갈 수 없음
"""


import sys
input = sys.stdin.readline

n = int(input())

# 인접 행렬 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드 워셜

# k : 중간에 거쳐가는 노드
for k in range(n):
    # i : 출발 노드
    for i in range(n):
        # j : 도착 노드
        for j in range(n):
            # i -> k, k -> j 가 가능하면 i -> j 도 가능
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# 출력
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()