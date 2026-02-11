"""
문제 번호: 10811
문제 이름: 바구니 뒤집기

1. 아이디어
- 시뮬레이션(구현) 문제
- 1부터 N까지 리스트를 생성
- M번 반복하면서
    - a ~ b 구간을 슬라이싱
    - [::-1]을 이용해 해당 구간을 뒤집어서 재할당

2. 시간복잡도
- 한 번 구간 뒤집기: O(N)
- 이를 M번 수행: O(N × M)
- N ≤ 100, M ≤ 1000
- 최악의 경우 100 × 1000 = 100,000 → 충분히 가능

3. 자료구조
N, M : int  (1<=N<=100, 1<=M<=1000)
- ans : 1부터 N까지의 리스트

"""

import sys

input = sys.stdin.readline

N, M = map(int,input().split())

ans = [i for i in range(1,N+1)]

for j in range(M):
    a, b =map(int,input().split())
    ans[a-1:b] = ans[a-1:b][::-1]

print(*ans)