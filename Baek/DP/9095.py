"""
1. 아이디어
- dp[x] = 정수 x를 1, 2, 3의 합으로 만드는 경우의 수
- 마지막에 올 수 있는 숫자는 1, 2, 3뿐
- 따라서 마지막 숫자를 기준으로 경우를 나누면
  dp[x] = dp[x-1] + dp[x-2] + dp[x-3]
- 여러 테스트케이스가 있으므로 입력값 중 최댓값(max_t)까지만
  DP를 한 번 계산해 재사용

2. 시간복잡도
- DP 계산: O(max_t)
- 출력: O(n)
- 전체 시간복잡도: O(max_t)

3. 자료구조
- DP 배열 dp : int[]
  dp[x]는 값 x에 대한 경우의 수를 저장
"""

import sys
input = sys.stdin.readline

n = int(input())
t = []

for _ in range(n):
    t.append(int(input()))

max_t = max(t)
dp = [0] * (max_t + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for i in range(5, max_t + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for x in t:
    print(dp[x])
