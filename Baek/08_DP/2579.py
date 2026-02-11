"""
1. 아이디어
- DP
- 연속 3칸을 밟을 수 없으므로, 현재 계단에 오는 경우는 2가지
  1) i-2에서 바로 i로 오는 경우
  2) i-3 -> i-1 -> i로 오는 경우
- 두 경우 중 점수가 최대인 값을 dp[i]에 저장

2. 시간복잡도
- DP 계산: O(N)
- 전체 시간복잡도: O(N)

3. 자료구조
- 계단 개수: int (N ≤ 300)
- 계단 점수: int 배열
- dp 배열: int 배열 (각 계단까지의 최대 점수)
"""

import sys
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]

# 예외 처리
if N == 1:
    print(stairs[0])
    exit()
if N == 2:
    print(stairs[0] + stairs[1])
    exit()

dp = [0] * N

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, N):
    dp[i] = max(
        dp[i-2] + stairs[i],
        dp[i-3] + stairs[i-1] + stairs[i]
    )

print(dp[N-1])
