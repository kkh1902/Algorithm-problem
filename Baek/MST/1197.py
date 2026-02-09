"""
1. 아이디어
- 간선을 인접리스트 형태로 저장
- 시작점부터 힙에 넣기
- 힙이 빌때 까지,
    - 해당 노드 방문 안한곳일 경우
    - 방문 체크, 비용 추가, 연결된 간선 새롭게 추가

2. 시간복잡도
- MST :O(ElogE)
- Edge리스트에 저장 : O(E)
- Heap 안 모든 Edge에 연결된 간선 확인 O(E+E)
- O(3E + ElogE) = O(ElogE) 

3. 자료구조
- Edge 저장 리스트 (int, int )[] 무게, 정점번호
    - 무게 최대 : 1e6 > INT 가능
    - 정점 번호 최대: 1e4 >INT 가능
- 정점 방문 : bool[]
- MST 비용 : int ( 최대 2^31 보다 이내)
"""

import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
edge = [[] for _ in range(V+1)]
chk = [False]*(V+1)
rs = 0
for i in range(E):
    a,b,c = map(int,input().split())
    edge[a].append([c,b])
    edge[b].append([c,a])

heap  = [[0,1]]

while heap:
    w,each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] = True
        rs+= w
        for next_edge in edge[each_node]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap,next_edge)

print(rs)
