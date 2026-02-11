"""
1. 아이디어
- 동전을 저장한뒤, 반대로 뒤집은
- 동전 for > 
    - 동전 사용한만큼 k값 갱신

2. 시간복잡도
- O(N)


3. 자료구조
- 동전 금액 : int[]
- 동전 사용 cnt : int
- 남은 금액 : int
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
cnt = 0

for each_coin in coins:
    cnt += k // each_coin
    k = k % each_coin

print(cnt)