"""
문제 1916 최소비용 구하기
1. 아이디어
- 한점 시작, 모든 거리 : 다익스트라
- 간선, 인접리스트 저장
- 거리배열 무한대 초기화
- 시작점 : 거리배열 0, 힙에 넣어주기
- 힙에서 빼면서 다음의 것들 수행
    - 최신값인지 먼저 확인
    - 간선을타고 간 비용이 더 작으면 갱신

2. 시간복잡도
- 다익스트라 : O (ElogV)
    - E : 3e5? M(1 ≤ M ≤ 100,000)
    - V : 2e4? N(1 ≤ N ≤ 1,000, lgv ~=
    - ElogV=   (100,000)log2(1000) 1,000,000> 가능

3. 자료구조
- 힙 : (비용, 노드번호)
- 거리 배열 : 비용 : int[]
- 간선 저장, 인접리스트 : (비용, 노드 번호)[]

"""

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V = int(input())
E = int(input())

edge = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for i in range(E):
    u,v,w= map(int,input().split())
    edge[u].append([w,v])

st , en  = map(int,input().split())

# 시작점 초기화 start 지점 힙에 (거리= 0, 노드=st)
dist[st]= 0
heap=[[0,st]]

while heap:
    ew, ev =heapq.heappop(heap)
    # 힙에서 나온값이 최신 최단거리인지확인
    # 이미 더 짧은 경로로 갱신된 경우 무시
    if dist[ev] != ew:
        continue
    # 현재 노드와 연결된 모든 인벚 노드 탐색
    for nw, nv in edge[ev]:
        # 현재 노드를 거쳐 가는 비용이 더 작으면 최단거리 갱신
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            # 갱신된 거리로 힙에 넣어 다음 탐색 대상으로 추가
            heapq.heappush(heap, [dist[nv],nv])


print(dist[en])