"""
1. 아이디어
- i,j k 값을 입력 받는다
- i,j,k 값을 for M 만큼 하면서 
- 슬라이스 슬라이딩 초기화
- 리스트의 값을 초기화 한다.  

2. 시간복잡도
- M번 반복: O(M)
- 1<=M <=100

3. 자료구조
- N, M : int N (1 ≤ N ≤ 100) M (1 ≤ M ≤ 100)
- tri : i,j,k list []
- basket : [0] * (n+1)

"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for t in range(i, j + 1):
        basket[t] = k

print(*basket[1:])

