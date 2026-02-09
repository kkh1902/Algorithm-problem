"""
# 1. 아이디어
- 모든 점 -> 모든점 : 플로이드 
- 비용배열 INF 초기화
- 간선의 비용 대입
- 거쳐서 비용 줄어들 경우, 갱신(for문 3번)

# 2. 시간복잡도
- 플로이드 : O(V^3)
- 1e6 >가능

# 3. 자료구조
- 비용 배열,  int [][]


"""
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
# 비용 배열 생성
rs = [[INF] *(n+1) for _ in range(n+1)]

# 같은 도시는 이동 비용 0
for i in range(1,n+1):
    rs[i][i] = 0

# 간선(버스) 정보 입력 중복 노선 있을 수 있으므로 가장 싼 비용만 저장
for i in range(m):
    a,b,c = map(int,input().split())
    rs[a][b]= min(rs[a][b],c)

# ==== 변수 초기화 완료 === #

# 로직 플로이드 핵심 (3중 for문)
for k in range(1,n+1): # 거치는 값  경유지
    for j in range(1,n+1): # 시작  출발도시
        for i in range(1,n+1): # 도착   도착 도시
            # j -> i 직접 가는 비용 j->k->i로 가는 비용  더 싼 걸로 교체
            # j에서 i로 가는데 k를 거쳐 가면 더 싸질까?
            if rs[j][i] > rs[j][k] + rs[k][i]:
                rs[j][i]= rs[j][k] + rs[k][i]

# 출력부  -> 모든 도시 쌍 출력
for j in range(1,n+1):
    for i in range(1,n+1):
        # 갈 수 없는 경우 문제 조건상 0 출력
        if rs[j][i] == INF: print(0, end=' ')
        # 갈 수 있으면 최소 비용 출력
        else : print(rs[j][i], end= ' ')
    print()