"""
1. 아이디어
- MST 문제이고 PRIM 알고리즘 사용
- 시작점 부터 힙에 넣기
- 힙이 빌떄 까지
    - 해당 노드 방문 안한곳일 경우 
    - 방문 체크, 비용추가, 연결된 간선 새롭게 추가

2. 시간복잡도
- MST  : O(ElogE)
- Edge 리스트에 저장 : O(E)
- Heap 안 모든 Edge에 연결된 간선 확인 O(E+E)
- O(3E + ElogE) = O(ElogE)

3. 자료구조
- 컴퓨터 수 : int 
- Edge 저장 리스트 (int,int) [] : 비용, 정점번호
    - 비용 최대:  10000 > INT 가능
- 정점 방문 : bool []
- MST 비용 : int (최대10^5 * 10^4  = 10^9)

"""

import sys
import heapq
input = sys.stdin.readline

n= int(input())
v = int(input())

edge = [[] for _ in range(n+1) ]
chk  = [False] * (n+1)
rs = 0
for i in range(v):
    a,b,c = map(int,input().split())
    edge[a].append([c,b])
    edge[b].append([c,a])

heap = [[0,1]]

while heap:
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] =True
        rs+=w

        for next_edge in edge[each_node]:
            if chk[next_edge[1]] ==False:
                heapq.heappush(heap,next_edge)

print(rs)